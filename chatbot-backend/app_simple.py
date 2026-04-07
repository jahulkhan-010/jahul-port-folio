from flask import Flask, request, jsonify

app = Flask(__name__)

# CORS Middleware - Add headers to ALL responses
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Max-Age'] = '3600'
    print(f"✅ CORS headers added: {request.method} {request.path}")
    return response

# Handle OPTIONS requests (CORS preflight)
@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        print(f"✅ OPTIONS request for: {request.path}")
        return jsonify({'status': 'ok'}), 200

# Knowledge base with answers
KNOWLEDGE_BASE = {
    'experience': "Jahul Khan has 4+ years of professional experience as an Angular Developer. He is currently working as a Senior Frontend Developer at V2F Technology (May 2023 - Present), where he leads the development of Visa2Fly platform serving 500,000+ users with 99.3% approval rate. Previously, he worked at IMG Global Infotech and Success Ladder Technologies.",
    
    'work': "Jahul is currently a Senior Frontend Developer at V2F Technology since May 2023, where he leads enterprise-scale application development. He previously worked as an Angular Developer at IMG Global Infotech (May 2022 - May 2023) and as an Angular Intern at Success Ladder Technologies (Feb 2022 - May 2022).",
    
    'skills': "Jahul is highly skilled in Angular 19, TypeScript, JavaScript (ES6+), HTML5, CSS3/SCSS, RxJS, and NgRx for state management. He has expertise in UI frameworks like Material Design, PrimeNG, Bootstrap, and Tailwind CSS. His toolkit includes Git, RESTful APIs, Responsive Design, and Webpack.",
    
    'visa2fly': "Visa2Fly is Jahul's flagship project - a comprehensive online visa application platform with AI-powered document validation, supporting 50+ countries, real-time tracking, and seamless payment integration. The platform has processed over 500,000 visa applications with an impressive 99.3% approval rate. Jahul architected 4 enterprise applications: Consumer Platform, B2B Portal, Agent Dashboard, and Admin Portal.",
    
    'project': "Jahul's main project is the Visa2Fly ecosystem, which includes Consumer Platform (visa2fly.com), B2B Vendor Portal (b2b.visa2fly.com), Agent Dashboard (dashboard.visa2fly.com), and Admin Portal (accounts.visa2fly.com). He also integrated 24+ white-label versions for partners like IndiGo, SpiceJet, ixigo, and EaseMyTrip.",
    
    'white-label': "Jahul successfully integrated Visa2Fly with 24+ leading travel and fintech brands including airlines (IndiGo, SpiceJet, Vistara), travel platforms (ixigo, EaseMyTrip, Yatra, Wego), and fintech companies (Niyo, ACKO Insurance, HDFC SmartBuy). He implemented multi-tenant architecture with custom theming for each partner.",
    
    'achievement': "Jahul's key achievements include: (1) Delivered enterprise apps serving 500,000+ users, (2) Achieved 99.3% visa approval rate, (3) Integrated 24+ white-label partners, (4) Improved performance by 40% through optimization, and (5) Led frontend architecture for multi-tenant platform.",
    
    'contact': "You can reach Jahul Khan at jahul.khan@visa2fly.com or jahulkhan010@gmail.com. Connect with him on LinkedIn and GitHub. His portfolio website is jahulkhan.dev.",
    
    'education': "Jahul is a skilled Angular developer with strong foundation in web development and modern frontend technologies. He continuously upgrades his skills through hands-on enterprise application development.",
    
    'frontend': "Jahul specializes in enterprise-scale Angular applications with focus on performance optimization, responsive design, and user experience. He has deep expertise in state management (RxJS, NgRx), reusable component libraries, micro-frontend architectures, and RESTful API integration.",
}

def find_answer(question):
    """Find best matching answer based on keywords"""
    question_lower = question.lower()
    
    # Check for keywords
    if any(word in question_lower for word in ['experience', 'work history', 'career', 'job']):
        return KNOWLEDGE_BASE['experience']
    elif any(word in question_lower for word in ['current', 'now', 'present', 'today']):
        return KNOWLEDGE_BASE['work']
    elif any(word in question_lower for word in ['skill', 'technology', 'tech stack', 'know']):
        return KNOWLEDGE_BASE['skills']
    elif any(word in question_lower for word in ['visa2fly', 'visa 2 fly', 'visa project']):
        return KNOWLEDGE_BASE['visa2fly']
    elif any(word in question_lower for word in ['project', 'built', 'developed', 'created']):
        return KNOWLEDGE_BASE['project']
    elif any(word in question_lower for word in ['white-label', 'white label', 'integration', 'partner']):
        return KNOWLEDGE_BASE['white-label']
    elif any(word in question_lower for word in ['achievement', 'accomplish', 'success']):
        return KNOWLEDGE_BASE['achievement']
    elif any(word in question_lower for word in ['contact', 'email', 'reach', 'connect']):
        return KNOWLEDGE_BASE['contact']
    elif any(word in question_lower for word in ['education', 'study', 'learn']):
        return KNOWLEDGE_BASE['education']
    elif any(word in question_lower for word in ['frontend', 'angular', 'expertise']):
        return KNOWLEDGE_BASE['frontend']
    else:
        return "I can help you learn about Jahul's work experience, technical skills, projects like Visa2Fly, white-label integrations, achievements, or how to contact him. What would you like to know?"

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    origin = request.headers.get('Origin', 'unknown')
    print(f"✅ Health check from: {origin}")
    return jsonify({
        'status': 'healthy',
        'message': 'Chatbot API is running',
        'cors': 'enabled',
        'version': 'simple'
    }), 200

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    try:
        data = request.get_json()
        user_question = data.get('question', '')
        
        if not user_question:
            return jsonify({'error': 'No question provided'}), 400
        
        print(f"✅ Question: {user_question}")
        answer = find_answer(user_question)
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
    print("="*70)
    print("🤖 Starting AI Chatbot Backend (Simple Version)")
    print(f"📚 Knowledge base loaded with {len(KNOWLEDGE_BASE)} categories")
    print("🚀 Server running on http://localhost:5000")
    print("🌐 CORS enabled for all origins")
    print("💡 Using keyword-based matching (fast & reliable)")
    print("="*70)
    print("")
    app.run(debug=True, port=5000, host='0.0.0.0')
