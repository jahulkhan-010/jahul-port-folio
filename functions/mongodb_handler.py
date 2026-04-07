"""
MongoDB Handler for Cloud Functions
"""

import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from datetime import datetime
from difflib import SequenceMatcher

class MongoDBHandler:
    def __init__(self):
        self.client = None
        self.db = None
        self.connected = False
        self.connect()
    
    def connect(self):
        """Connect to MongoDB Atlas"""
        try:
            uri = os.getenv('MONGODB_ATLAS_URI')
            db_name = os.getenv('MONGODB_ATLAS_DB', 'jahul_chatbot_prod')
            
            if not uri:
                print("⚠️  MongoDB URI not found in environment")
                return False
            
            print(f"🌐 Connecting to MongoDB Atlas (Production)...")
            
            self.client = MongoClient(
                uri,
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=10000
            )
            
            # Test connection
            self.client.admin.command('ping')
            self.db = self.client[db_name]
            self.connected = True
            
            print(f"✅ Connected to MongoDB: {db_name}")
            
            # Create indexes
            self._create_indexes()
            
            return True
            
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            print(f"❌ MongoDB Connection Failed: {e}")
            self.connected = False
            return False
        except Exception as e:
            print(f"❌ Error: {e}")
            self.connected = False
            return False
    
    def _create_indexes(self):
        """Create database indexes"""
        try:
            self.db.conversations.create_index('question_lower')
            self.db.conversations.create_index('timestamp')
            print("✅ Database indexes created")
        except Exception as e:
            print(f"⚠️  Index creation warning: {e}")
    
    def save_conversation(self, question, answer, source="ai_response"):
        """Save conversation to MongoDB"""
        if not self.connected:
            return False
        
        try:
            conversation = {
                'question': question,
                'answer': answer,
                'source': source,
                'timestamp': datetime.utcnow(),
                'question_lower': question.lower().strip(),
                'environment': 'production'
            }
            
            result = self.db.conversations.insert_one(conversation)
            print(f"✅ Saved conversation: {result.inserted_id}")
            return True
            
        except Exception as e:
            print(f"❌ Error saving: {e}")
            return False
    
    def find_similar_question(self, question, threshold=0.7):
        """Find similar question"""
        if not self.connected:
            return None
        
        try:
            question_lower = question.lower().strip()
            
            conversations = self.db.conversations.find({
                'question_lower': {'$regex': question_lower, '$options': 'i'}
            }).limit(10)
            
            best_match = None
            best_similarity = 0
            
            for conv in conversations:
                similarity = SequenceMatcher(
                    None, 
                    question_lower, 
                    conv['question_lower']
                ).ratio()
                
                if similarity > best_similarity and similarity >= threshold:
                    best_similarity = similarity
                    best_match = conv
            
            if best_match:
                print(f"🎯 Found match: {best_similarity:.2%}")
                return best_match['answer']
            
            return None
            
        except Exception as e:
            print(f"❌ Error finding similar: {e}")
            return None
    
    def get_stats(self):
        """Get statistics"""
        if not self.connected:
            return {'connected': False, 'error': 'Not connected'}
        
        try:
            total = self.db.conversations.count_documents({})
            return {
                'total_conversations': total,
                'connected': True,
                'environment': 'production'
            }
        except Exception as e:
            return {'connected': False, 'error': str(e)}

# Global instance
mongodb = MongoDBHandler()
