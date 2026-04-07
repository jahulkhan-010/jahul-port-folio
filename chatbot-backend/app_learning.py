from flask import Flask, request, jsonify
import json
import os
from datetime import datetime
from difflib import SequenceMatcher

app = Flask(__name__)

# File-based storage for learning (for local development)
CONVERSATIONS_FILE = 'conversations_history.json'

# CORS Middleware
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Max-Age'] = '3600'
    return response

@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200

# Load conversations from file
def load_conversations():
    """Load saved conversations from JSON file"""
    if os.path.exists(CONVERSATIONS_FILE):
        try:
            with open(CONVERSATIONS_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

# Save conversations to file
def save_conversations(conversations):
    """Save conversations to JSON file"""
    try:
        with open(CONVERSATIONS_FILE, 'w') as f:
            json.dump(conversations, f, indent=2)
    except Exception as e:
        print(f"Error saving: {e}")

# Calculate similarity between strings
def calculate_similarity(str1, str2):
    """Calculate similarity percentage between two strings"""
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio() * 100

# Save new conversation
def save_conversation(question, answer, source="predefined"):
    """Save Q&A pair for learning"""
    conversations = load_conversations()
    conversations.append({
        'question': question,
        'answer': answer,
        'source': source,
        'timestamp': datetime.now().isoformat(),
        'question_lower': question.lower().strip()
    })
    save_conversations(conversations)
    print(f"✅ Saved: {question[:50]}... → {answer[:50]}...")

# Find similar questions from history
def find_similar_questions(question, threshold=70):
    """Find similar questions from conversation history"""
    conversations = load_conversations()
    question_lower = question.lower().strip()
    
    best_match = None
    best_similarity = 0
    
    for conv in conversations:
        similarity = calculate_similarity(question_lower, conv.get('question_lower', ''))
        
        if similarity > best_similarity and similarity >= threshold:
            best_similarity = similarity
            best_match = conv
    
    if best_match:
        print(f"🎯 Found match: {best_similarity:.1f}% similar")
        print(f"   Question: {best_match['question']}")
        return best_match['answer']
    
    return None

# Base knowledge about Jahul Khan
KNOWLEDGE_BASE = {
    'name': "Jahul Khan - Senior Frontend Developer with 4+ years experience",
    'experience': "4+ years as Angular Developer at V2F Technology, IMG Global Infotech, Success Ladder Technologies",
    'skills': "Angular 19, TypeScript, JavaScript, RxJS, NgRx, HTML5, CSS3, Material Design, PrimeNG, Bootstrap, Tailwind CSS",
    'visa2fly': "Visa2Fly platform - 500,000+ users, 99.3% approval rate, 50+ countries, AI-powered document validation",
    'projects': "Visa2Fly ecosystem with 4 apps, 24+ white-label integrations (IndiGo, SpiceJet, ixigo, EaseMyTrip)",
    'white-label': "24+ partners: IndiGo, SpiceJet, Vistara, ixigo, EaseMyTrip, Yatra, Wego, Niyo, ACKO, HDFC SmartBuy, Paytm",
    'achievements': "500K users, 99.3% approval, 40% performance improvement, 60% faster load, 24+ integrations",
    'contact': "Email: jahul.khan@visa2fly.com, jahulkhan010@gmail.com | LinkedIn, GitHub | Portfolio: jahulkhan.dev",
    'email': "jahul.khan@visa2fly.com (work), jahulkhan010@gmail.com (personal)",
    'linkedin': "Connect on LinkedIn - search 'Jahul Khan' for professional profile",
    'github': "Active on GitHub with Angular projects, TypeScript utilities, UI components",
    'location': "Based in India, available for remote work worldwide",
    'current': "Senior Frontend Developer at V2F Technology since May 2023",
}

# Find answer with AI learning
def find_answer(question):
    """Smart answer finder with learning capability"""
    q = question.lower().strip()

    # Step 1: Check learned conversations (70% similarity threshold)
    learned_answer = find_similar_questions(q, threshold=70)
    if learned_answer:
        print("💡 Using learned answer")
        return learned_answer

    # Step 2: Check base knowledge with pattern matching
    # Personal
    if any(w in q for w in ['who is', 'who are', 'about', 'introduce', 'tell me']):
        return f"{KNOWLEDGE_BASE['name']}. {KNOWLEDGE_BASE['experience']}"

    # Experience
    elif any(w in q for w in ['experience', 'work', 'career', 'job', 'years']):
        return KNOWLEDGE_BASE['experience']

    # Skills
    elif any(w in q for w in ['skill', 'technology', 'tech', 'know', 'angular', 'typescript']):
        return KNOWLEDGE_BASE['skills']

    # Visa2Fly - ALL variations
    elif any(p in q for p in ['visa2fly', 'visa 2 fly', 'visa2fly', 'visa-2-fly', 'visatofly', 'v2f', 'flagship']):
        return KNOWLEDGE_BASE['visa2fly']

    # White-label - ALL typos and variations
    elif any(p in q for p in ['white-label', 'white label', 'whitelabel', 'white-lable', 'whitelable', 'whitelables',
                               'whitelabels', 'wite label', 'whit label', 'partner', 'integration',
                               'indigo', 'spicejet', 'ixigo', 'easemytrip', 'yatra']):
        return KNOWLEDGE_BASE['white-label']

    # Projects
    elif any(w in q for w in ['project', 'built', 'developed', 'portfolio', 'work on']):
        return KNOWLEDGE_BASE['projects']

    # Achievements
    elif any(w in q for w in ['achievement', 'accomplish', 'success', 'metric', 'number']):
        return KNOWLEDGE_BASE['achievements']

    # Contact - ALL variations
    elif any(w in q for w in ['contact', 'email', 'mail', 'reach', 'hire', 'get in touch']):
        return KNOWLEDGE_BASE['contact']

    # Email specific
    elif any(w in q for w in ['email', 'e-mail', 'gmail', 'mail address']):
        return KNOWLEDGE_BASE['email']

    # LinkedIn - ALL typos
    elif any(p in q for p in ['linkedin', 'linked in', 'linkedln', 'linkdin', 'link in']):
        return KNOWLEDGE_BASE['linkedin']

    # GitHub - ALL variations
    elif any(p in q for p in ['github', 'git hub', 'githb', 'git', 'code', 'repo']):
        return KNOWLEDGE_BASE['github']

    # Location
    elif any(w in q for w in ['location', 'where', 'based', 'live', 'from']):
        return KNOWLEDGE_BASE['location']

    # Current job
    elif any(w in q for w in ['current', 'now', 'present', 'today', 'currently']):
        return KNOWLEDGE_BASE['current']

    # Step 3: If no match, try lower similarity threshold (50%)
    fallback_answer = find_similar_questions(q, threshold=50)
    if fallback_answer:
        print("🔍 Using fallback match (lower threshold)")
        return fallback_answer

    # Step 4: Default response
    return "I'd love to help! I can answer questions about Jahul Khan's: Experience, Skills, Projects (Visa2Fly, White-label integrations), Contact info (Email, LinkedIn, GitHub), Current role, Location, and more. What would you like to know?"

@app.route('/api/health', methods=['GET'])
def health():
    """Health check"""
    conv_count = len(load_conversations())
    print(f"✅ Health check - {conv_count} conversations learned")
    return jsonify({
        'status': 'healthy',
        'message': 'AI Learning Chatbot is running',
        'learned_conversations': conv_count,
        'learning': True
    }), 200

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat endpoint with learning"""
    try:
        data = request.get_json()
        question = data.get('question', '')

        if not question:
            return jsonify({'error': 'No question provided'}), 400

        print(f"\n📤 Question: {question}")

        # Get answer
        answer = find_answer(question)

        # Save conversation for learning
        save_conversation(question, answer, source="ai_response")

        print(f"📥 Answer: {answer[:100]}...")

        return jsonify({
            'response': answer,
            'status': 'success',
            'learning': True,
            'total_learned': len(load_conversations())
        }), 200

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/api/stats', methods=['GET'])
def stats():
    """Get learning statistics"""
    conversations = load_conversations()
    return jsonify({
        'total_conversations': len(conversations),
        'unique_questions': len(set(c['question_lower'] for c in conversations)),
        'learning_active': True
    }), 200

if __name__ == '__main__':
    print("")
    print("="*80)
    print("🧠 AI Learning Chatbot - Dynamic Training System")
    print("="*80)
    print(f"📚 Base Knowledge: {len(KNOWLEDGE_BASE)} categories")
    print(f"💾 Learned Conversations: {len(load_conversations())}")
    print("🎯 Features:")
    print("   • Learns from every conversation")
    print("   • 70% similarity matching")
    print("   • Fallback to 50% for broader matches")
    print("   • Saves all Q&A pairs")
    print("   • Gets smarter over time")
    print("")
    print("🚀 Server: http://localhost:5001")
    print("🌐 CORS: Enabled")
    print("⚡ Learning: Active")
    print("="*80)
    print("")
    print("Ready to learn and answer! 🎉")
    print("")
    app.run(debug=True, port=5001, host='0.0.0.0')

