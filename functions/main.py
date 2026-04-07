from firebase_functions import https_fn
from firebase_admin import initialize_app
import json
import os
from datetime import datetime
from difflib import SequenceMatcher
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Initialize Firebase Admin
app = initialize_app()

# MongoDB Configuration
MONGODB_URI = os.getenv('MONGODB_ATLAS_URI', '')
MONGODB_DB = os.getenv('MONGODB_ATLAS_DB', 'jahul_chatbot_prod')

# Initialize MongoDB
mongodb_client = None
mongodb_db = None
USE_MONGODB = False

try:
    if MONGODB_URI:
        print("🌐 Connecting to MongoDB Atlas...")
        mongodb_client = MongoClient(
            MONGODB_URI,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=10000
        )
        # Test connection
        mongodb_client.admin.command('ping')
        mongodb_db = mongodb_client[MONGODB_DB]

        # Create indexes
        mongodb_db.conversations.create_index('question_lower')
        mongodb_db.conversations.create_index('timestamp')

        USE_MONGODB = True
        print(f"✅ Connected to MongoDB: {MONGODB_DB}")
    else:
        print("⚠️  No MongoDB URI provided")
except Exception as e:
    print(f"⚠️  MongoDB connection failed: {e}")
    print("   Using base knowledge only")
    USE_MONGODB = False

# Comprehensive Knowledge base about Jahul Khan
KNOWLEDGE_BASE = {
    # Personal Information
    'name': "Jahul Khan is a Senior Frontend Developer and Angular specialist with 4+ years of professional experience in building enterprise-scale web applications.",
    'about': "Jahul Khan is a passionate Senior Frontend Developer specializing in Angular development with 4+ years of experience. He currently works at V2F Technology, where he leads the development of the Visa2Fly platform - a comprehensive visa application system serving over 500,000 users with a 99.3% approval rate. Jahul is known for his expertise in building scalable, high-performance web applications using Angular 19, TypeScript, and modern frontend technologies.",
    'bio': "Jahul Khan is an accomplished Angular Developer with a proven track record in enterprise application development. He has successfully delivered multiple large-scale projects, including the Visa2Fly ecosystem with 4 enterprise applications and 24+ white-label integrations. His expertise spans across Angular 19, TypeScript, RxJS, NgRx, and modern UI frameworks.",
    
    # Professional Experience
    'experience': "Jahul Khan has 4+ years of professional experience as an Angular Developer. Currently serving as Senior Frontend Developer at V2F Technology (May 2023 - Present), he leads the development of the Visa2Fly platform serving 500,000+ users with a 99.3% approval rate. Previously, he worked as Angular Developer at IMG Global Infotech (May 2022 - May 2023) and as Angular Intern at Success Ladder Technologies (Feb 2022 - May 2022).",
    'current_job': "Jahul is currently working as Senior Frontend Developer at V2F Technology since May 2023. He leads the development of enterprise-scale applications, specifically the Visa2Fly platform, responsible for architecting frontend solutions, implementing state management, and ensuring optimal performance.",
    'work': "At V2F Technology (May 2023 - Present), Jahul leads frontend development for Visa2Fly platform. At IMG Global Infotech (May 2022 - May 2023), he developed e-commerce platforms. At Success Ladder Technologies (Feb 2022 - May 2022), he started as an intern.",
    'responsibilities': "Leading frontend architecture, implementing NgRx state management, developing reusable components, integrating RESTful APIs, optimizing performance (40% improvement), code review and mentoring, responsive design implementation, managing 24+ white-label integrations, ensuring cross-browser compatibility, and maintaining code quality.",
    
    # Technical Skills
    'skills': "Angular 19, TypeScript, JavaScript ES6+, HTML5, CSS3/SCSS, RxJS, NgRx, Material Design, PrimeNG, Bootstrap, Tailwind CSS, Git, RESTful APIs, Responsive Design, Webpack, Jest, Jasmine, Karma, npm/yarn, Agile/Scrum, CI/CD, Performance Optimization.",
    'technologies': "Frontend: Angular 19, TypeScript, JavaScript, HTML5, CSS3, RxJS, NgRx | UI: Material Design, PrimeNG, Bootstrap, Tailwind | Tools: Git, Webpack, npm | Testing: Jest, Jasmine, Karma | APIs: RESTful services",
    'angular': "Expert in Angular 19: Component architecture, Dependency injection, RxJS operators, NgRx state management, Angular Router, Forms, HTTP Client, Material Design, Lazy loading, Change detection, Custom directives, Animations, Standalone components, Signals, Performance optimization.",
    'typescript': "Advanced TypeScript: Strong typing, Generics, Decorators, OOP concepts, Type guards, Enums, Async/await, ES6+ features, Module system.",
    'tools': "VS Code, WebStorm, Chrome DevTools, Postman, Git/GitHub/GitLab, Jira, Trello, Slack, Teams, Zoom, Figma, Adobe XD, Jest, Cypress, Jenkins, GitHub Actions, AWS, Firebase, Netlify.",
    
    # Projects
    'visa2fly': "Visa2Fly - flagship project serving 500,000+ users with 99.3% approval rate. Features: AI-powered document validation, 50+ countries support, real-time tracking, payment integration, multi-language support, mobile-responsive design. Includes 4 applications: Consumer Platform, B2B Portal, Agent Dashboard, Admin Portal, plus 24+ white-label integrations.",
    'projects': "Visa2Fly Ecosystem (4 apps, 500K users), White-Label Integrations (24+ partners), B2B Vendor Portal, Admin Dashboard, Agent Portal. Built with Angular 19, TypeScript, NgRx.",
    'white-label': "Successfully integrated with 24+ brands: Airlines (IndiGo, SpiceJet, Vistara, Air India Express, AirAsia) | Travel (ixigo, EaseMyTrip, Yatra, Wego, Cleartrip, Goibibo) | Fintech (Niyo, ACKO Insurance, HDFC SmartBuy, Paytm, PhonePe) | Hotels (Treebo, FabHotels) | Others (Mobikwik, Amazon Pay, Google Pay, Freecharge). Multi-tenant architecture with custom theming.",
    'consumer_platform': "Visa2Fly Consumer Platform (visa2fly.com): Step-by-step wizard, document upload, real-time tracking, payment integration, country-specific requirements, mobile-responsive, multi-language, live chat, email notifications.",
    'b2b_portal': "B2B Vendor Portal (b2b.visa2fly.com): Bulk processing, custom pricing, white-label branding, API integration, analytics, sub-agent management, credit system, invoicing, performance reports.",
    
    # Achievements & Metrics
    'achievements': "500,000+ users served, 99.3% approval rate, 24+ white-label partners, 4 enterprise apps, 40% performance improvement, 60% faster page loads, 35% bug reduction, 95%+ code coverage, zero critical bugs, mentored 5+ developers.",
    'metrics': "500,000+ users, 99.3% approval, 50+ countries, 24+ partners, 4 apps, 40% faster performance, 60% better load time, 35% fewer bugs, 95%+ test coverage, 1000+ daily active users, 10,000+ monthly applications.",
    
    # Contact & Social
    'contact': "Email: jahul.khan@visa2fly.com (work), jahulkhan010@gmail.com (personal). LinkedIn, GitHub, Portfolio: jahulkhan.dev. Based in India, available for remote work, freelance, consulting, mentoring.",
    'email': "Professional: jahul.khan@visa2fly.com | Personal: jahulkhan010@gmail.com. Responds within 24 hours.",
    'linkedin': "Connect on LinkedIn for professional journey, endorsements, recommendations, latest updates. Search 'Jahul Khan' or visit through portfolio.",
    'github': "Active GitHub profile with Angular projects, TypeScript utilities, UI components, code samples. Check coding style and contributions.",
    'social': "Active on LinkedIn (professional networking), GitHub (code repos), Portfolio (jahulkhan.dev), Twitter (tech discussions), Stack Overflow (community help).",
    
    # Location & Availability
    'location': "Based in India, works internationally across time zones. Remote collaboration expert using Slack, Teams, Zoom. Agile methodologies.",
    'available': "Currently at V2F Technology, open to: Freelance Angular projects, technical consulting, code review, mentoring, part-time work, speaking engagements, technical writing.",

    # Hobbies & Interests
    'hobby': "Jahul's hobbies include coding personal projects, learning new technologies and frameworks, contributing to open-source projects, reading tech blogs and documentation, attending tech meetups and conferences, experimenting with new Angular features, mentoring junior developers, and staying updated with web development trends.",
    'hobbies': "Outside of work, Jahul enjoys: Coding side projects to explore new technologies, Contributing to open-source Angular libraries, Reading technical books and blogs, Attending developer meetups and conferences, Learning about new frontend frameworks and tools, Helping other developers through mentoring and code reviews, Experimenting with web performance optimization techniques.",
    'interests': "Jahul is interested in: Angular ecosystem and latest features, Frontend architecture patterns, State management solutions, Performance optimization techniques, Component design systems, Web accessibility (a11y), Progressive Web Apps (PWA), Micro-frontend architectures, TypeScript advanced patterns, Cloud deployment strategies, DevOps for frontend apps.",
    
    # Work Style
    'methodology': "Agile/Scrum: Daily standups, TDD, code reviews, pair programming, CI/CD, Git flow, documentation-first, performance monitoring, user feedback, continuous improvement.",
    'softskills': "Excellent communication, team leadership, problem-solving, time management, attention to detail, adaptability, mentoring, client relations, critical thinking, creative solutions.",
    'languages': "English (Fluent), Hindi (Native). Programming: TypeScript, JavaScript, HTML, CSS/SCSS.",
    
    # Company & Industry
    'company': "V2F Technology (Visa2Fly) - leading visa tech company with 24+ partnerships, 500,000+ users, 99.3% approval rate.",
    'industry': "Travel Technology and Fintech: Visa/immigration tech, travel booking, B2B solutions, white-label SaaS, payment integration, document automation, CRM, analytics.",
    
    # Education & Goals
    'education': "Strong foundation in Computer Science and Web Development. IT education with continuous upskilling through courses, certifications, hands-on experience. Lifelong learner.",
    'certifications': "Angular Advanced, TypeScript Mastery, RxJS Programming, NgRx State Management, Performance Optimization, Web Accessibility, Agile/Scrum, AWS Cloud. Regular webinars and conferences.",
    'learning': "Exploring: Angular 19 Signals, Micro-frontends, PWAs, Web Components, GraphQL, Angular Universal, Advanced RxJS, Web performance, Accessibility, Cloud deployment.",
    'specialization': "Enterprise Angular apps, Multi-tenant SaaS, E-commerce, Travel tech, Fintech, Real-time dashboards, State management, Performance optimization, White-label solutions, Responsive design, PWAs, Component libraries.",
    'expertise': "Angular 19 architecture, TypeScript patterns, RxJS, NgRx, Performance (40% improvement), Responsive design, API integration, Component-driven development, Micro-frontends, Testing, CI/CD, Code review, Mentoring.",
    'goals': "Angular expert and thought leader, open-source contribution, international speaking, own SaaS product, mentoring developers, technical writing, full-stack with Node.js, cloud architecture, staying at frontend forefront.",
    'passion': "Beautiful UIs, solving challenges, optimizing performance, exceptional UX, teaching, open-source, new technologies, code quality, accessibility, continuous learning.",
}

def calculate_similarity(str1, str2):
    """Calculate similarity between two strings (0-100)"""
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio() * 100

def save_conversation(question, answer, source="ai_response"):
    """Save conversation to MongoDB for learning"""
    if not USE_MONGODB or not mongodb_db:
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

        result = mongodb_db.conversations.insert_one(conversation)
        print(f"✅ Saved to MongoDB: {result.inserted_id}")
        return True
    except Exception as e:
        print(f"❌ Error saving conversation: {e}")
        return False

def find_similar_questions(question, threshold=70):
    """Find similar questions from MongoDB"""
    if not USE_MONGODB or not mongodb_db:
        return None

    try:
        question_lower = question.lower().strip()

        # Get recent conversations
        conversations = list(mongodb_db.conversations.find().limit(100))

        best_match = None
        best_similarity = 0

        for conv in conversations:
            similarity = calculate_similarity(question_lower, conv.get('question_lower', ''))

            if similarity > best_similarity and similarity >= threshold:
                best_similarity = similarity
                best_match = conv

        if best_match:
            print(f"🎯 Found similar question: {best_similarity:.1f}% match")
            return best_match['answer']

        return None
    except Exception as e:
        print(f"❌ Error finding similar questions: {e}")
        return None

def find_answer(question):
    """Find best matching answer - Base knowledge first, then learning"""
    q = question.lower().strip()

    # Use base knowledge FIRST for common questions
    # This ensures ALL users get proper responses

    # Personal & About
    if any(w in q for w in ['who is', 'who are', 'about jahul', 'introduce']):
        return KNOWLEDGE_BASE['about']
    elif any(w in q for w in ['bio', 'biography', 'background', 'profile']):
        return KNOWLEDGE_BASE['bio']
    
    # Experience
    elif any(w in q for w in ['experience', 'work history', 'career', 'years']):
        return KNOWLEDGE_BASE['experience']
    elif any(w in q for w in ['current job', 'current role', 'present job']):
        return KNOWLEDGE_BASE['current_job']
    elif any(w in q for w in ['responsibility', 'duties', 'role']):
        return KNOWLEDGE_BASE['responsibilities']
    
    # Skills
    elif any(w in q for w in ['skill', 'technology', 'tech stack']):
        return KNOWLEDGE_BASE['skills']
    elif 'angular' in q:
        return KNOWLEDGE_BASE['angular']
    elif any(w in q for w in ['typescript', 'ts']):
        return KNOWLEDGE_BASE['typescript']
    
    # Projects - Visa2Fly variations
    elif any(p in q for p in ['visa2fly', 'visa 2 fly', 'visa2fly', 'visa-2-fly', 'visa 2fly', 'visatofly', 'v2f', 'flagship']):
        return KNOWLEDGE_BASE['visa2fly']
    elif any(w in q for w in ['project', 'built', 'developed', 'portfolio']):
        return KNOWLEDGE_BASE['projects']
    
    # White-label - ALL variations and typos
    elif any(p in q for p in ['white-label', 'white label', 'whitelabel', 'white-lable', 'whitelable', 'whitelables', 'whitelabels', 'wite label', 'whit label', 'integration', 'partner', 'indigo', 'spicejet', 'ixigo', 'easemytrip']):
        return KNOWLEDGE_BASE['white-label']
    
    elif 'b2b' in q or 'vendor' in q:
        return KNOWLEDGE_BASE['b2b_portal']
    elif 'consumer' in q:
        return KNOWLEDGE_BASE['consumer_platform']
    
    # Achievements
    elif any(w in q for w in ['achievement', 'accomplish', 'success']):
        return KNOWLEDGE_BASE['achievements']
    elif any(w in q for w in ['metric', 'number', 'stat', 'how many']):
        return KNOWLEDGE_BASE['metrics']
    
    # Contact - ALL variations
    elif any(w in q for w in ['contact', 'email', 'mail', 'reach', 'hire']):
        return KNOWLEDGE_BASE['contact']
    elif any(w in q for w in ['email', 'e-mail', 'gmail']):
        return KNOWLEDGE_BASE['email']
    elif any(p in q for p in ['linkedin', 'linked in', 'linkedln', 'linkdin']):
        return KNOWLEDGE_BASE['linkedin']
    elif any(p in q for p in ['github', 'git hub', 'githb', 'git', 'code', 'repo']):
        return KNOWLEDGE_BASE['github']
    elif any(w in q for w in ['social', 'facebook', 'instagram', 'twitter']):
        return KNOWLEDGE_BASE['social']
    
    # Other
    elif any(w in q for w in ['location', 'where', 'based', 'live']):
        return KNOWLEDGE_BASE['location']
    elif any(w in q for w in ['available', 'freelance', 'consulting']):
        return KNOWLEDGE_BASE['available']
    elif any(w in q for w in ['goal', 'future', 'plan']):
        return KNOWLEDGE_BASE['goals']
    elif any(w in q for w in ['passion', 'passionate', 'love']):
        return KNOWLEDGE_BASE['passion']

    # Hobbies & Interests
    elif any(p in q for p in ['hobby', 'hobbies', 'free time', 'spare time', 'leisure', 'do for fun', 'outside work']):
        return KNOWLEDGE_BASE['hobby']
    elif any(w in q for w in ['hobbies', 'activities', 'pastime']):
        return KNOWLEDGE_BASE['hobbies']
    elif any(w in q for w in ['interest', 'interests', 'interested in']):
        return KNOWLEDGE_BASE['interests']

    # If no base knowledge match, try learned conversations
    else:
        learned_answer = find_similar_questions(q, threshold=70)
        if learned_answer:
            return learned_answer

        # Final fallback - guide the user
        return "I can help you learn about Jahul Khan! Ask about his: Work Experience, Technical Skills (Angular, TypeScript), Projects (Visa2Fly, White-label integrations), Achievements, Contact Info (Email, LinkedIn, GitHub), Hobbies, Interests, Education, Goals, and more!"

@https_fn.on_request(cors=https_fn.CorsOptions(cors_origins="*", cors_methods=["GET", "POST", "OPTIONS"]))
def chatbot(req: https_fn.Request) -> https_fn.Response:
    """Cloud Function for chatbot API"""
    
    # Health check
    if req.method == "GET" and req.path == "/health":
        stats = {}
        if USE_MONGODB and mongodb_db:
            try:
                total = mongodb_db.conversations.count_documents({})
                stats = {
                    'total_conversations': total,
                    'mongodb_connected': True
                }
            except:
                stats = {'mongodb_connected': False}
        else:
            stats = {'mongodb_connected': False}

        return https_fn.Response(
            json.dumps({
                "status": "healthy",
                "message": "Chatbot API is running",
                "cors": "enabled",
                "mongodb": USE_MONGODB,
                "stats": stats
            }),
            status=200,
            headers={"Content-Type": "application/json"}
        )
    
    # Chat endpoint
    if req.method == "POST":
        try:
            data = req.get_json()
            question = data.get("question", "")
            
            if not question:
                return https_fn.Response(
                    json.dumps({"error": "No question provided"}),
                    status=400,
                    headers={"Content-Type": "application/json"}
                )
            
            answer = find_answer(question)

            # Save conversation for learning
            save_conversation(question, answer, source="ai_response")

            return https_fn.Response(
                json.dumps({
                    "response": answer,
                    "status": "success",
                    "learning": True
                }),
                status=200,
                headers={"Content-Type": "application/json"}
            )
        
        except Exception as e:
            return https_fn.Response(
                json.dumps({"error": str(e), "status": "error"}),
                status=500,
                headers={"Content-Type": "application/json"}
            )
    
    return https_fn.Response(
        json.dumps({"error": "Method not allowed"}),
        status=405,
        headers={"Content-Type": "application/json"}
    )
