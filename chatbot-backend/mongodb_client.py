"""
MongoDB Client for AI Chatbot
Handles both local and production databases
"""

import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MongoDBClient:
    def __init__(self):
        self.environment = os.getenv('ENVIRONMENT', 'development')
        self.client = None
        self.db = None
        self.connected = False
        self.connect()
    
    def connect(self):
        """Connect to MongoDB based on environment"""
        try:
            if self.environment == 'production':
                # Use MongoDB Atlas for production
                uri = os.getenv('MONGODB_ATLAS_URI')
                db_name = os.getenv('MONGODB_ATLAS_DB', 'jahul_chatbot_prod')
                print(f"🌐 Connecting to MongoDB Atlas (Production)...")
            elif self.environment == 'atlas':
                # Use MongoDB Atlas for development (cloud)
                uri = os.getenv('MONGODB_ATLAS_URI')
                db_name = 'jahul_chatbot_dev'
                print(f"🌐 Connecting to MongoDB Atlas (Development Cloud)...")
            else:
                # Use local MongoDB for development
                uri = os.getenv('MONGODB_LOCAL_URI', 'mongodb://localhost:27017/')
                db_name = os.getenv('MONGODB_LOCAL_DB', 'jahul_chatbot')
                print(f"💻 Connecting to Local MongoDB (Development)...")
            
            # Create MongoDB client with SSL/TLS settings
            self.client = MongoClient(
                uri,
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=10000,
                tls=True,
                tlsAllowInvalidCertificates=True  # Fix for SSL handshake on Render/Python 3.14
            )
            
            # Test connection
            self.client.admin.command('ping')
            
            # Get database
            self.db = self.client[db_name]
            
            print(f"✅ Connected to MongoDB: {db_name}")
            print(f"📊 Environment: {self.environment}")

            # Set connected flag
            self.connected = True

            # Create indexes
            self._create_indexes()

            return True
            
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            print(f"❌ MongoDB Connection Failed: {e}")
            print(f"⚠️  Falling back to JSON file storage")
            self.connected = False
            return False
        except Exception as e:
            print(f"❌ Error: {e}")
            self.connected = False
            return False
    
    def _create_indexes(self):
        """Create database indexes for better performance"""
        try:
            # Index on question_lower for faster searching
            self.db.chat_bot_collection.create_index('question_lower')
            # Index on timestamp for sorting
            self.db.chat_bot_collection.create_index('timestamp')
            # Index on source
            self.db.chat_bot_collection.create_index('source')
            print("✅ Database indexes created")
        except Exception as e:
            print(f"⚠️  Index creation warning: {e}")
    
    def save_conversation(self, question, answer, source="ai_response"):
        """Save conversation to MongoDB"""
        try:
            conversation = {
                'question': question,
                'answer': answer,
                'source': source,
                'timestamp': datetime.utcnow(),
                'question_lower': question.lower().strip(),
                'environment': self.environment
            }

            result = self.db.chat_bot_collection.insert_one(conversation)
            print(f"✅ Saved conversation: {result.inserted_id}")
            return True

        except Exception as e:
            print(f"❌ Error saving conversation: {e}")
            return False
    
    def get_all_conversations(self, limit=100):
        """Get all conversations"""
        try:
            conversations = list(
                self.db.chat_bot_collection
                .find()
                .sort('timestamp', -1)
                .limit(limit)
            )
            return conversations
        except Exception as e:
            print(f"❌ Error getting conversations: {e}")
            return []
    
    def find_similar_question(self, question, threshold=0.7):
        """Find similar question using advanced text search"""
        try:
            question_lower = question.lower().strip()

            # Get all conversations
            conversations = list(self.db.chat_bot_collection.find().limit(1000))

            if not conversations:
                return None

            # Calculate similarity for all conversations
            from difflib import SequenceMatcher

            best_match = None
            best_similarity = 0

            for conv in conversations:
                # Calculate similarity
                similarity = SequenceMatcher(
                    None,
                    question_lower,
                    conv.get('question_lower', '')
                ).ratio()

                # Check for keyword matches (boost score)
                question_words = set(question_lower.split())
                conv_words = set(conv.get('question_lower', '').split())
                common_words = question_words & conv_words

                if len(common_words) > 0:
                    keyword_boost = len(common_words) / max(len(question_words), 1) * 0.3
                    similarity += keyword_boost

                if similarity > best_similarity and similarity >= threshold:
                    best_similarity = similarity
                    best_match = conv

            if best_match:
                print(f"🎯 Found similar question: {best_similarity:.2%} match")
                print(f"   Q: {best_match.get('question', '')[:50]}...")
                return best_match.get('answer', '')

            return None

        except Exception as e:
            print(f"❌ Error finding similar question: {e}")
            return None

    def search_by_keywords(self, keywords):
        """Search conversations by keywords"""
        try:
            results = []
            for keyword in keywords:
                docs = self.db.chat_bot_collection.find({
                    '$or': [
                        {'question_lower': {'$regex': keyword, '$options': 'i'}},
                        {'answer': {'$regex': keyword, '$options': 'i'}}
                    ]
                }).limit(5)
                results.extend(list(docs))

            return results
        except Exception as e:
            print(f"❌ Error searching: {e}")
            return []

    def update_answer(self, question, new_answer):
        """Update existing answer"""
        try:
            question_lower = question.lower().strip()
            result = self.db.chat_bot_collection.update_many(
                {'question_lower': question_lower},
                {'$set': {'answer': new_answer, 'updated_at': datetime.utcnow()}}
            )
            print(f"✅ Updated {result.modified_count} answers")
            return result.modified_count > 0
        except Exception as e:
            print(f"❌ Error updating: {e}")
            return False
    
    def get_stats(self):
        """Get database statistics"""
        try:
            total = self.db.chat_bot_collection.count_documents({})
            by_source = list(self.db.chat_bot_collection.aggregate([
                {'$group': {'_id': '$source', 'count': {'$sum': 1}}}
            ]))

            return {
                'total_conversations': total,
                'by_source': {item['_id']: item['count'] for item in by_source},
                'environment': self.environment,
                'connected': True
            }
        except Exception as e:
            print(f"❌ Error getting stats: {e}")
            return {
                'total_conversations': 0,
                'connected': False,
                'error': str(e)
            }
    
    def close(self):
        """Close MongoDB connection"""
        if self.client:
            self.client.close()
            print("✅ MongoDB connection closed")

# Create global MongoDB client instance
mongodb_client = MongoDBClient()
