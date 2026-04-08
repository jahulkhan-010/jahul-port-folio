"""
Dynamic AI Chatbot - Learns from Every Conversation
Uses MongoDB for persistent storage and learning
Works for ANY person - fully customizable!
"""

from flask import Flask, request, jsonify
from mongodb_client import mongodb_client
import os
from datetime import datetime

app = Flask(__name__)

# Check if MongoDB is available
USE_MONGODB = mongodb_client.db is not None

print(f"{'='*80}")
print(f"🧠 DYNAMIC AI CHATBOT - MongoDB Learning System")
print(f"{'='*80}")
print(f"💾 MongoDB Status: {'✅ Connected' if USE_MONGODB else '❌ Not Connected'}")
print(f"🌐 Environment: {os.getenv('ENVIRONMENT', 'development')}")
print(f"⚡ Learning Mode: FULLY DYNAMIC")
print(f"{'='*80}")

# CORS Middleware
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Max-Age'] = '3600'
    return response

@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200

# Default base knowledge (fallback only)
DEFAULT_RESPONSES = {
    'greeting': "Hello! I'm an AI assistant. I learn from every conversation! Ask me anything and I'll remember it.",
    'help': "I can help you with anything you teach me! Just ask questions and I'll learn from our conversation.",
    'unknown': "I don't have information about that yet, but I'm learning! Can you tell me more so I can remember for next time?"
}

def extract_keywords(text):
    """Extract keywords from text"""
    # Remove common words
    stop_words = {'the', 'is', 'at', 'which', 'on', 'a', 'an', 'as', 'are', 'was', 'were', 
                  'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                  'would', 'should', 'could', 'may', 'might', 'must', 'can', 'about', 'what',
                  'who', 'where', 'when', 'why', 'how', 'your', 'my', 'his', 'her', 'their'}
    
    words = text.lower().split()
    keywords = [w for w in words if w not in stop_words and len(w) > 2]
    return keywords

def find_answer(question):
    """Find answer using smart fuzzy matching"""

    if not USE_MONGODB:
        return DEFAULT_RESPONSES['unknown']

    try:
        question_lower = question.lower().strip()
        print(f"🔍 Searching for: '{question_lower}'")

        # Get all documents from MongoDB
        all_docs = list(mongodb_client.db.chat_bot_collection.find({}))
        total_docs = len(all_docs)
        print(f"📊 Total documents in collection: {total_docs}")

        if total_docs == 0:
            print(f"⚠️ No documents found in database!")
            return DEFAULT_RESPONSES['unknown']

        # Step 1: Try EXACT match (any field)
        for doc in all_docs:
            q_lower = (doc.get('question_lower') or doc.get('Question_Lower') or doc.get('question', '')).lower()
            if q_lower == question_lower:
                print(f"✅ EXACT match: '{doc.get('question')}'")
                return doc.get('answer', DEFAULT_RESPONSES['unknown'])

        # Step 2: Try PARTIAL match - if question contains key words
        question_words = set(question_lower.split())
        print(f"� Question words: {question_words}")

        best_match = None
        best_score = 0

        for doc in all_docs:
            q_text = (doc.get('question_lower') or doc.get('Question_Lower') or doc.get('question', '')).lower()
            doc_words = set(q_text.split())

            # Calculate word overlap
            common_words = question_words.intersection(doc_words)
            if len(common_words) > 0:
                # Score based on percentage of matching words
                score = len(common_words) / max(len(question_words), len(doc_words))
                print(f"   � '{doc.get('question')}' -> {len(common_words)} common words, score: {score:.2f}")

                if score > best_score:
                    best_score = score
                    best_match = doc

        # If we found ANY word match, return it
        if best_match and best_score >= 0.3:  # At least 30% word overlap
            print(f"✅ PARTIAL match (score {best_score:.2f}): '{best_match.get('question')}'")
            return best_match.get('answer', DEFAULT_RESPONSES['unknown'])
        
        # Step 2: Try similarity search (70% threshold)
        similar_answer = mongodb_client.find_similar_question(question, threshold=0.70)
        if similar_answer:
            print(f"✅ Similar question found!")
            return similar_answer
        
        # Step 3: Try keyword search (50% threshold)
        similar_answer = mongodb_client.find_similar_question(question, threshold=0.50)
        if similar_answer:
            print(f"✅ Keyword match found!")
            return similar_answer
        
        # Step 4: Search by keywords
        keywords = extract_keywords(question)
        if keywords:
            results = mongodb_client.search_by_keywords(keywords)
            if results:
                print(f"✅ Keyword results found: {len(results)}")
                # Return the most recent answer
                return results[0].get('answer', DEFAULT_RESPONSES['unknown'])
        
        # Step 5: Check for greetings
        greetings = ['hi', 'hello', 'hey', 'greetings']
        if any(g in question_lower for g in greetings):
            return DEFAULT_RESPONSES['greeting']
        
        # Step 6: Default unknown response
        return DEFAULT_RESPONSES['unknown']
    
    except Exception as e:
        print(f"❌ Error in find_answer: {e}")
        return DEFAULT_RESPONSES['unknown']

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    stats = mongodb_client.get_stats() if USE_MONGODB else {'connected': False}
    
    return jsonify({
        'status': 'healthy',
        'message': 'Dynamic AI Chatbot - MongoDB Learning System',
        'mongodb_connected': USE_MONGODB,
        'learning_mode': 'FULLY DYNAMIC',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'stats': stats
    }), 200

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat endpoint with dynamic learning"""
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({'error': 'No question provided'}), 400
        
        print(f"\n{'='*80}")
        print(f"📤 INCOMING QUESTION: {question}")
        print(f"{'='*80}")
        
        # Get answer from dynamic learning system
        answer = find_answer(question)
        
        # Save conversation to MongoDB for learning
        if USE_MONGODB:
            saved = mongodb_client.save_conversation(
                question=question,
                answer=answer,
                source='dynamic_ai'
            )
            
            if saved:
                print(f"💾 Conversation saved to MongoDB")
                stats = mongodb_client.get_stats()
                print(f"📊 Total conversations in DB: {stats.get('total_conversations', 0)}")
        
        print(f"📥 RESPONSE: {answer[:100]}...")
        print(f"{'='*80}\n")
        
        return jsonify({
            'response': answer,
            'status': 'success',
            'learning': True,
            'mongodb': USE_MONGODB
        }), 200
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/api/teach', methods=['POST'])
def teach():
    """Teach the chatbot new information"""
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        answer = data.get('answer', '').strip()
        
        if not question or not answer:
            return jsonify({'error': 'Both question and answer required'}), 400
        
        if not USE_MONGODB:
            return jsonify({'error': 'MongoDB not connected'}), 503
        
        print(f"\n📚 TEACHING MODE")
        print(f"Question: {question}")
        print(f"Answer: {answer[:100]}...")
        
        # Save to MongoDB
        saved = mongodb_client.save_conversation(
            question=question,
            answer=answer,
            source='user_taught'
        )
        
        if saved:
            stats = mongodb_client.get_stats()
            return jsonify({
                'status': 'success',
                'message': 'Successfully taught! I will remember this.',
                'total_learned': stats.get('total_conversations', 0)
            }), 200
        else:
            return jsonify({'error': 'Failed to save'}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def stats():
    """Get learning statistics"""
    if USE_MONGODB:
        stats = mongodb_client.get_stats()
        return jsonify(stats), 200
    else:
        return jsonify({'error': 'MongoDB not connected', 'connected': False}), 503

if __name__ == '__main__':
    print("")
    print("🚀 Server starting...")
    print(f"📍 URL: http://localhost:5001")
    print(f"🌐 CORS: Enabled for all origins")
    print(f"⚡ Mode: Dynamic Learning")
    print("")
    print("Ready to learn from conversations! 🎉")
    print("")
    
    app.run(debug=True, port=5001, host='0.0.0.0')
