from flask import Flask, request, jsonify
from mongodb_client import mongodb_client
import os

app = Flask(__name__)

# Check if MongoDB is available
USE_MONGODB = mongodb_client.db is not None

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

# Comprehensive knowledge base about Jahul Khan
KNOWLEDGE_BASE = {
    # Personal & About
    'name': "Jahul Khan - Senior Frontend Developer with 4+ years of professional experience specializing in Angular development.",
    'about': "Jahul Khan is a passionate Senior Frontend Developer with 4+ years of experience building enterprise-scale web applications. Currently at V2F Technology, he leads the Visa2Fly platform development serving 500,000+ users with 99.3% approval rate.",
    
    # Professional
    'experience': "Jahul has 4+ years of professional experience: Senior Frontend Developer at V2F Technology (May 2023-Present) leading Visa2Fly platform, Angular Developer at IMG Global Infotech (May 2022-May 2023), and Angular Intern at Success Ladder Technologies (Feb 2022-May 2022).",
    'current': "Currently working as Senior Frontend Developer at V2F Technology since May 2023, leading Visa2Fly platform serving 500,000+ users with 99.3% approval rate.",
    
    # Technical Skills
    'skills': "Expert in Angular 19, TypeScript, JavaScript ES6+, HTML5, CSS3/SCSS, RxJS, NgRx, Material Design, PrimeNG, Bootstrap, Tailwind CSS, Git, RESTful APIs, MongoDB, Firebase.",
    'angular': "Deep expertise in Angular 19: Component architecture, RxJS, NgRx state management, Angular Router, Forms, HTTP Client, Material Design, Performance optimization.",
    
    # Projects
    'visa2fly': "Visa2Fly - flagship project with 500,000+ users, 99.3% approval rate, 50+ countries supported. Features AI-powered validation, real-time tracking, payment integration.",
    'projects': "Visa2Fly Ecosystem (4 apps), 24+ White-label integrations (IndiGo, SpiceJet, ixigo, EaseMyTrip), B2B Portal, Admin Dashboard.",
    'white-label': "24+ partner integrations: Airlines (IndiGo, SpiceJet, Vistara), Travel (ixigo, EaseMyTrip, Yatra, Wego), Fintech (Niyo, ACKO, HDFC SmartBuy, Paytm).",
    
    # Achievements
    'achievements': "500,000+ users served, 99.3% approval rate, 24+ white-label partners, 40% performance improvement, 60% faster page loads, zero critical bugs.",
    
    # Contact
    'contact': "Email: jahul.khan@visa2fly.com (work), jahulkhan010@gmail.com (personal). LinkedIn, GitHub, Portfolio: jahulkhan.dev.",
    'email': "Professional: jahul.khan@visa2fly.com | Personal: jahulkhan010@gmail.com",
    'linkedin': "Find Jahul Khan on LinkedIn for professional profile, endorsements, and latest updates.",
    'github': "Active GitHub with Angular projects, TypeScript utilities, UI component libraries.",
    
    # Personal
    'hobby': "Jahul's hobbies: coding personal projects, learning new technologies, contributing to open-source, attending tech meetups, mentoring developers.",
    'passion': "Passionate about beautiful UIs, solving challenges, optimizing performance, exceptional UX, teaching, open-source, continuous learning.",
    
    # Location
    'location': "Based in India, available for remote work worldwide. Experienced in remote collaboration.",
    'goals': "Become Angular expert, contribute to open-source, speak at conferences, build SaaS product, mentor developers.",
}

def find_answer(question):
    """Find answer with MongoDB learning + base knowledge"""
    q = question.lower().strip()
    
    # Step 1: Try MongoDB learned conversations (if available)
    if USE_MONGODB:
        learned_answer = mongodb_client.find_similar_question(q, threshold=0.7)
        if learned_answer:
            print("💡 Using MongoDB learned answer")
            return learned_answer
    
    # Step 2: Check base knowledge
    # Personal
    if any(w in q for w in ['who is', 'who are', 'about', 'introduce', 'tell me']):
        return KNOWLEDGE_BASE['about']
    elif any(w in q for w in ['experience', 'work', 'career', 'job', 'years']):
        return KNOWLEDGE_BASE['experience']
    elif any(w in q for w in ['current', 'now', 'present', 'today']):
        return KNOWLEDGE_BASE['current']
    
    # Skills
    elif any(w in q for w in ['skill', 'technology', 'tech', 'know', 'angular', 'typescript']):
        return KNOWLEDGE_BASE['skills']
    elif 'angular' in q:
        return KNOWLEDGE_BASE['angular']
    
    # Projects
    elif any(p in q for p in ['visa2fly', 'visa 2 fly', 'v2f', 'flagship']):
        return KNOWLEDGE_BASE['visa2fly']
    elif any(p in q for p in ['white-label', 'white label', 'whitelabel', 'whitelable', 'whitelables', 'partner', 'integration', 'indigo', 'spicejet', 'ixigo']):
        return KNOWLEDGE_BASE['white-label']
    elif any(w in q for w in ['project', 'built', 'developed', 'portfolio']):
        return KNOWLEDGE_BASE['projects']
    
    # Achievements
    elif any(w in q for w in ['achievement', 'accomplish', 'success', 'metric']):
        return KNOWLEDGE_BASE['achievements']
    
    # Contact
    elif any(w in q for w in ['contact', 'email', 'mail', 'reach', 'hire']):
        return KNOWLEDGE_BASE['contact']
    elif any(w in q for w in ['email', 'e-mail', 'gmail']):
        return KNOWLEDGE_BASE['email']
    elif any(p in q for p in ['linkedin', 'linked in', 'linkedln', 'linkdin']):
        return KNOWLEDGE_BASE['linkedin']
    elif any(p in q for p in ['github', 'git hub', 'git', 'code', 'repo']):
        return KNOWLEDGE_BASE['github']
    
    # Personal
    elif any(p in q for p in ['hobby', 'hobbies', 'free time', 'do for fun']):
        return KNOWLEDGE_BASE['hobby']
    elif any(w in q for w in ['passion', 'passionate', 'love', 'enjoy']):
        return KNOWLEDGE_BASE['passion']
    
    # Location & Goals
    elif any(w in q for w in ['location', 'where', 'based', 'live']):
        return KNOWLEDGE_BASE['location']
    elif any(w in q for w in ['goal', 'future', 'plan']):
        return KNOWLEDGE_BASE['goals']
    
    # Fallback
    else:
        return "I can help you learn about Jahul Khan! Ask about his: Experience, Skills (Angular, TypeScript), Projects (Visa2Fly, White-label), Contact (Email, LinkedIn, GitHub), Hobbies, Goals, and more!"

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    stats = mongodb_client.get_stats() if USE_MONGODB else {'connected': False}
    
    return jsonify({
        'status': 'healthy',
        'message': 'AI Chatbot with MongoDB',
        'mongodb_connected': USE_MONGODB,
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'stats': stats
    }), 200

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat endpoint with MongoDB learning"""
    try:
        data = request.get_json()
        question = data.get('question', '')
        
        if not question:
            return jsonify({'error': 'No question provided'}), 400
        
        print(f"\n📤 Question: {question}")
        
        # Get answer
        answer = find_answer(question)
        
        # Save to MongoDB (if available)
        if USE_MONGODB:
            mongodb_client.save_conversation(question, answer, source="ai_response")
            print(f"💾 Saved to MongoDB")
        
        print(f"📥 Answer: {answer[:100]}...")
        
        return jsonify({
            'response': answer,
            'status': 'success',
            'mongodb': USE_MONGODB
        }), 200
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/api/stats', methods=['GET'])
def stats():
    """Get MongoDB statistics"""
    if USE_MONGODB:
        stats = mongodb_client.get_stats()
        return jsonify(stats), 200
    else:
        return jsonify({
            'error': 'MongoDB not connected',
            'connected': False
        }), 503

if __name__ == '__main__':
    print("")
    print("="*80)
    print("🧠 AI Chatbot with MongoDB Integration")
    print("="*80)
    print(f"📚 Base Knowledge: {len(KNOWLEDGE_BASE)} categories")
    print(f"💾 MongoDB: {'✅ Connected' if USE_MONGODB else '❌ Not Connected'}")
    print(f"🌐 Environment: {os.getenv('ENVIRONMENT', 'development')}")
    print("")
    print("🚀 Server: http://localhost:5001")
    print("🌐 CORS: Enabled")
    print("⚡ Learning: MongoDB-based")
    print("="*80)
    print("")
    app.run(debug=True, port=5001, host='0.0.0.0')
