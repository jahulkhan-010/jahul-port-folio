from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Simple CORS configuration - handle manually for full control
@app.after_request
def after_request(response):
    """Add CORS headers to every response"""
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
    response.headers['Access-Control-Max-Age'] = '3600'
    return response

@app.before_request
def handle_preflight():
    """Handle OPTIONS preflight requests"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        response.headers['Access-Control-Max-Age'] = '3600'
        return response, 200

# Load pre-trained sentence transformer model for semantic search
model = SentenceTransformer('all-MiniLM-L6-v2')

# Portfolio knowledge base - Your data
KNOWLEDGE_BASE = [
    {
        "category": "work_experience",
        "question": "What is Jahul's work experience?",
        "answer": "Jahul Khan has 4+ years of professional experience as an Angular Developer. He is currently working as a Senior Frontend Developer at V2F Technology (May 2023 - Present), where he leads the development of Visa2Fly platform. Previously, he worked as an Angular Developer at IMG Global Infotech (May 2022 - May 2023) and as an Angular Intern at Success Ladder Technologies (Feb 2022 - May 2022)."
    },
    {
        "category": "current_role",
        "question": "What is Jahul's current role?",
        "answer": "Jahul is currently a Senior Frontend Developer at V2F Technology, where he has been working since May 2023. In this role, he leads the development of enterprise-scale applications and has successfully delivered the Visa2Fly platform serving over 500,000 users."
    },
    {
        "category": "technical_skills",
        "question": "What are Jahul's technical skills?",
        "answer": "Jahul is highly skilled in Angular 19, TypeScript, JavaScript (ES6+), HTML5, CSS3/SCSS, RxJS, and NgRx for state management. He also has expertise in UI frameworks like Material Design, PrimeNG, Bootstrap, and Tailwind CSS. His technical toolkit includes Git, RESTful APIs, Responsive Design, State Management, and Webpack. He follows Agile/Scrum methodologies and practices CI/CD, Test-Driven Development, and Code Review."
    },
    {
        "category": "visa2fly_project",
        "question": "Tell me about the Visa2Fly project",
        "answer": "Visa2Fly is Jahul's flagship project - a comprehensive online visa application platform with AI-powered document validation, priority processing, support for 50+ countries, real-time tracking, and seamless payment integration. The platform has processed over 500,000 visa applications with an impressive 99.3% approval rate. Jahul architected and implemented 4 enterprise applications: Consumer Platform, B2B Portal, Agent Dashboard, and Admin Portal."
    },
    {
        "category": "white_label_integrations",
        "question": "What white-label integrations has Jahul worked on?",
        "answer": "Jahul has successfully integrated the Visa2Fly platform with 24+ leading travel and fintech brands including major airlines like IndiGo, SpiceJet, and Vistara, as well as travel platforms like ixigo, EaseMyTrip, and Yatra. He also integrated with fintech companies like Niyo, ACKO Insurance, and HDFC SmartBuy. He implemented a multi-tenant architecture with custom theming and configurations for each partner."
    },
    {
        "category": "achievements",
        "question": "What are Jahul's key achievements?",
        "answer": "Jahul's key achievements include: (1) Successfully delivered enterprise-scale applications serving 500,000+ users, (2) Achieved 99.3% visa approval rate through optimized user experience and validation, (3) Integrated 24+ white-label partner solutions for leading airlines and travel platforms, (4) Improved application performance by 40% through code optimization, and (5) Led frontend architecture decisions for multi-tenant platform."
    },
    {
        "category": "contact_information",
        "question": "How can I contact Jahul?",
        "answer": "You can reach Jahul Khan at jahul.khan@visa2fly.com or jahulkhan010@gmail.com. You can also connect with him on LinkedIn and GitHub. His portfolio website is jahulkhan.dev where you can find more information about his work and download his resume."
    },
    {
        "category": "frontend_expertise",
        "question": "What is Jahul's expertise in frontend development?",
        "answer": "Jahul specializes in enterprise-scale Angular applications with a focus on performance optimization, responsive design, and user experience. He has deep expertise in building complex state management systems using RxJS and NgRx, creating reusable component libraries, implementing micro-frontend architectures, and integrating with RESTful APIs. He's particularly skilled in building multi-tenant platforms with custom theming."
    },
    {
        "category": "education_background",
        "question": "What is Jahul's educational background?",
        "answer": "Jahul is a skilled Angular developer with a strong foundation in web development and modern frontend technologies. He has continuously upgraded his skills through hands-on experience in enterprise applications and stays current with the latest Angular versions and best practices."
    },
    {
        "category": "projects_portfolio",
        "question": "What projects has Jahul built?",
        "answer": "Jahul's main project is the Visa2Fly ecosystem, which includes multiple enterprise applications: the Consumer Platform (visa2fly.com), B2B Vendor Portal (b2b.visa2fly.com), Agent Dashboard (dashboard.visa2fly.com), and Admin Portal (accounts.visa2fly.com). He has also developed 24+ white-label versions of the platform for various partners in the travel and fintech industries."
    }
]

# Pre-compute embeddings for knowledge base
knowledge_embeddings = model.encode([item["question"] + " " + item["answer"] for item in KNOWLEDGE_BASE])

def find_best_answer(user_question):
    """Find the most relevant answer using semantic similarity"""
    # Encode user question
    question_embedding = model.encode([user_question])
    
    # Calculate cosine similarity
    similarities = cosine_similarity(question_embedding, knowledge_embeddings)[0]
    
    # Get the index of the most similar question
    best_match_idx = np.argmax(similarities)
    best_similarity = similarities[best_match_idx]
    
    # If similarity is above threshold, return the answer
    if best_similarity > 0.3:  # Threshold for relevance
        return KNOWLEDGE_BASE[best_match_idx]["answer"]
    else:
        return "I can help you learn about Jahul's work experience, technical skills, projects like Visa2Fly, white-label integrations, achievements, or how to contact him. What would you like to know?"

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests from frontend"""
    try:
        data = request.get_json()
        user_question = data.get('question', '')

        if not user_question:
            return jsonify({'error': 'No question provided'}), 400

        # Find best answer using ML
        answer = find_best_answer(user_question)

        print(f"✅ Question: {user_question}")
        print(f"✅ Answer: {answer[:50]}...")

        return jsonify({
            'response': answer,
            'status': 'success'
        }), 200

    except Exception as e:
        print(f"❌ Error in chat endpoint: {str(e)}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    print("✅ Health check called from:", request.headers.get('Origin', 'unknown'))
    return jsonify({
        'status': 'healthy',
        'message': 'Chatbot API is running',
        'cors': 'enabled'
    }), 200

if __name__ == '__main__':
    print("🤖 Starting AI Chatbot Backend...")
    print("📚 Knowledge base loaded with", len(KNOWLEDGE_BASE), "entries")
    print("🚀 Server running on http://localhost:5000")
    app.run(debug=True, port=5000)
