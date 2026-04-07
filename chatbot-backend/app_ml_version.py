from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# CORS Middleware - Add headers to ALL responses
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Max-Age'] = '3600'
    print(f"✅ CORS headers added to response: {request.method} {request.path}")
    return response

# Handle OPTIONS requests (CORS preflight)
@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        print(f"✅ OPTIONS request received for: {request.path}")
        response = jsonify({'status': 'ok'})
        return response, 200

print("🔧 Loading ML model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ ML model loaded!")

# Knowledge base
KNOWLEDGE_BASE = [
    {
        "category": "work_experience",
        "question": "What is Jahul's work experience?",
        "answer": "Jahul Khan has 4+ years of professional experience as an Angular Developer. He is currently working as a Senior Frontend Developer at V2F Technology (May 2023 - Present), where he leads the development of Visa2Fly platform. Previously, he worked as an Angular Developer at IMG Global Infotech (May 2022 - May 2023) and as an Angular Intern at Success Ladder Technologies (Feb 2022 - May 2022)."
    },
    {
        "category": "technical_skills",
        "question": "What are Jahul's technical skills?",
        "answer": "Jahul is highly skilled in Angular 19, TypeScript, JavaScript (ES6+), HTML5, CSS3/SCSS, RxJS, and NgRx for state management. He also has expertise in UI frameworks like Material Design, PrimeNG, Bootstrap, and Tailwind CSS. His technical toolkit includes Git, RESTful APIs, Responsive Design, State Management, and Webpack."
    },
    {
        "category": "visa2fly_project",
        "question": "Tell me about the Visa2Fly project",
        "answer": "Visa2Fly is Jahul's flagship project - a comprehensive online visa application platform with AI-powered document validation, priority processing, support for 50+ countries, real-time tracking, and seamless payment integration. The platform has processed over 500,000 visa applications with an impressive 99.3% approval rate."
    },
    {
        "category": "contact_information",
        "question": "How can I contact Jahul?",
        "answer": "You can reach Jahul Khan at jahul.khan@visa2fly.com or jahulkhan010@gmail.com. You can also connect with him on LinkedIn and GitHub."
    },
]

# Pre-compute embeddings
print("🔧 Computing knowledge base embeddings...")
knowledge_embeddings = model.encode([item["question"] + " " + item["answer"] for item in KNOWLEDGE_BASE])
print("✅ Knowledge base ready!")

def find_best_answer(user_question):
    """Find the most relevant answer using semantic similarity"""
    question_embedding = model.encode([user_question])
    similarities = cosine_similarity(question_embedding, knowledge_embeddings)[0]
    best_match_idx = np.argmax(similarities)
    best_similarity = similarities[best_match_idx]
    
    if best_similarity > 0.3:
        return KNOWLEDGE_BASE[best_match_idx]["answer"]
    else:
        return "I can help you learn about Jahul's work experience, technical skills, projects like Visa2Fly, or how to contact him. What would you like to know?"

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    print(f"✅ Health check from: {request.headers.get('Origin', 'unknown')}")
    return jsonify({
        'status': 'healthy',
        'message': 'Chatbot API is running',
        'cors': 'enabled'
    }), 200

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests from frontend"""
    try:
        data = request.get_json()
        user_question = data.get('question', '')
        
        if not user_question:
            return jsonify({'error': 'No question provided'}), 400
        
        print(f"✅ Question: {user_question}")
        answer = find_best_answer(user_question)
        print(f"✅ Answer: {answer[:50]}...")
        
        return jsonify({
            'response': answer,
            'status': 'success'
        }), 200
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

if __name__ == '__main__':
    print("")
    print("="*60)
    print("🤖 Starting AI Chatbot Backend...")
    print(f"📚 Knowledge base loaded with {len(KNOWLEDGE_BASE)} entries")
    print("🚀 Server running on http://localhost:5000")
    print("🌐 CORS enabled for all origins")
    print("="*60)
    print("")
    app.run(debug=True, port=5000, host='0.0.0.0')
