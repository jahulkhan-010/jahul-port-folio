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

# Comprehensive Knowledge base with detailed answers about Jahul Khan
KNOWLEDGE_BASE = {
    # Personal Information
    'name': "Jahul Khan is a Senior Frontend Developer and Angular specialist with 4+ years of professional experience in building enterprise-scale web applications.",

    'about': "Jahul Khan is a passionate Senior Frontend Developer specializing in Angular development with 4+ years of experience. He currently works at V2F Technology, where he leads the development of the Visa2Fly platform - a comprehensive visa application system serving over 500,000 users with a 99.3% approval rate. Jahul is known for his expertise in building scalable, high-performance web applications using Angular 19, TypeScript, and modern frontend technologies.",

    'bio': "Jahul Khan is an accomplished Angular Developer with a proven track record in enterprise application development. He has successfully delivered multiple large-scale projects, including the Visa2Fly ecosystem with 4 enterprise applications and 24+ white-label integrations. His expertise spans across Angular 19, TypeScript, RxJS, NgRx, and modern UI frameworks. Jahul is passionate about creating exceptional user experiences and optimizing application performance.",

    # Professional Experience
    'experience': "Jahul Khan has 4+ years of professional experience as an Angular Developer. Currently serving as Senior Frontend Developer at V2F Technology (May 2023 - Present), he leads the development of the Visa2Fly platform serving 500,000+ users with a 99.3% approval rate. Previously, he worked as Angular Developer at IMG Global Infotech (May 2022 - May 2023) building e-commerce solutions, and as Angular Intern at Success Ladder Technologies (Feb 2022 - May 2022) where he started his professional journey.",

    'current_job': "Jahul is currently working as Senior Frontend Developer at V2F Technology since May 2023. In this role, he leads the development of enterprise-scale applications, specifically the Visa2Fly platform. He is responsible for architecting frontend solutions, implementing state management, integrating RESTful APIs, and ensuring optimal performance across all applications. He also mentors junior developers and conducts code reviews to maintain high code quality standards.",

    'work': "At V2F Technology (May 2023 - Present), Jahul leads frontend development for Visa2Fly platform. At IMG Global Infotech (May 2022 - May 2023), he developed e-commerce platforms and enhanced user interfaces. At Success Ladder Technologies (Feb 2022 - May 2022), he started as an intern working on Angular components and learning enterprise development practices.",

    'responsibilities': "Jahul's current responsibilities include: Leading frontend architecture design, Implementing complex state management using NgRx, Developing reusable component libraries, Integrating RESTful APIs and third-party services, Optimizing application performance (achieved 40% improvement), Code review and mentoring team members, Implementing responsive designs for mobile and desktop, Managing white-label partner integrations (24+ partners), Ensuring cross-browser compatibility, and Writing unit tests and maintaining code quality.",

    # Technical Skills
    'skills': "Jahul is highly skilled in Angular 19, TypeScript, JavaScript (ES6+), HTML5, CSS3/SCSS, RxJS, and NgRx for state management. He has expertise in UI frameworks like Material Design, PrimeNG, Bootstrap, and Tailwind CSS. His technical toolkit includes Git, RESTful APIs, Responsive Design, State Management, Webpack, Jest, Jasmine, Karma for testing, npm/yarn for package management, Agile/Scrum methodologies, CI/CD pipelines, Code Review practices, and Performance Optimization techniques.",

    'technologies': "Frontend: Angular 19, TypeScript, JavaScript ES6+, HTML5, CSS3/SCSS, RxJS, NgRx | UI Frameworks: Material Design, PrimeNG, Bootstrap, Tailwind CSS | Tools: Git, Webpack, npm, yarn, VS Code | Testing: Jest, Jasmine, Karma | APIs: RESTful services, HTTP Client | Other: Responsive Design, Cross-browser compatibility, Performance optimization, Accessibility (WCAG), SEO optimization",

    'angular': "Jahul is an expert in Angular 19 with deep knowledge of: Component architecture and lifecycle hooks, Dependency injection and services, RxJS operators and reactive programming, NgRx for state management, Angular Router for navigation, Forms (Reactive and Template-driven), HTTP Client for API integration, Angular Material and PrimeNG, Lazy loading and code splitting, Change detection strategies, Custom directives and pipes, Angular animations, Standalone components, Signals (new in Angular), and Performance optimization techniques.",

    'typescript': "Jahul has advanced TypeScript skills including: Strong typing and interfaces, Generics and utility types, Decorators and metadata, Advanced OOP concepts, Type guards and type assertions, Enums and union types, Async/await and Promises, ES6+ features, Module system, and TypeScript configuration optimization.",

    # Projects
    'visa2fly': "Visa2Fly is Jahul's flagship project - a comprehensive online visa application platform serving 500,000+ users with a 99.3% approval rate. The platform features: AI-powered document validation, Support for 50+ countries, Real-time application tracking, Seamless payment integration with multiple gateways, Priority processing options, Multi-language support, Mobile-responsive design, Admin dashboard with analytics, B2B vendor portal, Agent management system, and 24+ white-label partner integrations. Jahul architected 4 enterprise applications: Consumer Platform (visa2fly.com), B2B Vendor Portal (b2b.visa2fly.com), Agent Dashboard (dashboard.visa2fly.com), and Admin Portal (accounts.visa2fly.com).",

    'projects': "Major Projects: (1) Visa2Fly Ecosystem - 4 enterprise applications serving 500,000+ users with 99.3% approval rate, (2) White-Label Integrations - 24+ partner integrations including IndiGo, SpiceJet, Vistara, ixigo, EaseMyTrip, (3) B2B Vendor Portal - Complete vendor management system with custom workflows, (4) Admin Dashboard - Comprehensive analytics and management platform, (5) Agent Portal - Multi-level agent hierarchy with commission management. All projects built with Angular 19, TypeScript, NgRx, and modern UI frameworks.",

    'white-label': "Jahul successfully integrated Visa2Fly with 24+ leading brands: Airlines - IndiGo, SpiceJet, Vistara, Air India Express, AirAsia India | Travel Platforms - ixigo, EaseMyTrip, Yatra, Wego, Cleartrip, Goibibo | Fintech - Niyo, ACKO Insurance, HDFC SmartBuy, Paytm, PhonePe | Hotels - Treebo Hotels, FabHotels | Other Partners - Mobikwik, Amazon Pay, Google Pay, Freecharge. He implemented multi-tenant architecture with custom theming, branding, and configurations for each partner.",

    'consumer_platform': "The Visa2Fly Consumer Platform (visa2fly.com) is a user-friendly visa application portal featuring: Step-by-step application wizard, Document upload with validation, Real-time status tracking, Payment integration, Country-specific requirements, Mobile-responsive design, Multi-language support, Live chat support, Email notifications, and User dashboard. Built with Angular 19, Material Design, and optimized for performance.",

    'b2b_portal': "The B2B Vendor Portal (b2b.visa2fly.com) enables travel agents and vendors to manage visa applications at scale. Features include: Bulk application processing, Custom pricing and commissions, White-label branding, API integration, Analytics dashboard, Sub-agent management, Credit system, Invoice generation, and Performance reports. This system handles thousands of applications daily.",

    # Achievements & Metrics
    'achievements': "Jahul's key achievements include: (1) Delivered enterprise applications serving 500,000+ users with 99.3% visa approval rate, (2) Successfully integrated 24+ white-label partner solutions including major airlines and travel platforms, (3) Improved application performance by 40% through code optimization and lazy loading, (4) Led frontend architecture decisions for multi-tenant platform, (5) Reduced page load time by 60% through performance optimization, (6) Implemented comprehensive state management reducing bugs by 35%, (7) Mentored 5+ junior developers, (8) Achieved 95%+ code coverage through unit testing, (9) Built reusable component library used across all 4 applications, (10) Delivered projects on time with zero critical bugs in production.",

    'metrics': "Platform Metrics: 500,000+ total users, 99.3% visa approval rate, 50+ countries supported, 24+ white-label partners, 4 enterprise applications, 40% performance improvement, 60% faster page load time, 35% bug reduction, 95%+ code test coverage, Zero critical production bugs, 1000+ daily active users, 10,000+ applications processed monthly.",

    # Contact & Social Media
    'contact': "You can reach Jahul Khan through multiple channels: Email: jahul.khan@visa2fly.com (work) or jahulkhan010@gmail.com (personal), LinkedIn: Connect on LinkedIn for professional networking, GitHub: Check out his code repositories and open-source contributions, Portfolio: Visit jahulkhan.dev for complete portfolio, Location: Based in India, Available for: Remote work, Freelance projects, Consulting opportunities, Technical mentoring.",

    'email': "Jahul Khan's email addresses: Professional: jahul.khan@visa2fly.com (for work-related inquiries), Personal: jahulkhan010@gmail.com (for general contact). He typically responds within 24 hours during business days.",

    'linkedin': "Connect with Jahul Khan on LinkedIn to see his professional journey, endorsements, recommendations, and latest updates. He regularly shares insights about Angular development, frontend best practices, and web development trends. Search for 'Jahul Khan' on LinkedIn or visit his profile through his portfolio website.",

    'github': "Jahul Khan maintains an active GitHub profile showcasing his code quality and technical expertise. His repositories include Angular projects, TypeScript utilities, UI component libraries, and code samples. Check out his GitHub to see his coding style, contribution history, and open-source involvement.",

    'social': "Jahul Khan is active on professional platforms: LinkedIn for professional networking and industry insights, GitHub for code repositories and open-source contributions, Portfolio website (jahulkhan.dev) for showcasing projects, Twitter for tech discussions and updates, Stack Overflow for helping the developer community. He believes in knowledge sharing and continuous learning.",

    # Location & Availability
    'location': "Jahul Khan is based in India and works with international clients across different time zones. He is experienced in remote collaboration, uses tools like Slack, Teams, Zoom for communication, and follows Agile methodologies for project management. Available for remote opportunities worldwide.",

    'available': "Jahul Khan is currently employed as Senior Frontend Developer at V2F Technology but is open to: Freelance Angular projects, Technical consulting opportunities, Code review and mentoring, Part-time consulting work, Speaking at tech events, Writing technical blog posts. For availability and rates, contact him via email.",

    # Work Style & Methodology
    'methodology': "Jahul follows Agile/Scrum methodologies with: Daily standups and sprint planning, Test-driven development (TDD), Code reviews and pair programming, CI/CD for automated deployments, Git flow for version control, Documentation-first approach, Performance monitoring, User feedback integration, Continuous improvement mindset.",

    'tools': "Development Tools: VS Code, WebStorm, Chrome DevTools, Postman | Version Control: Git, GitHub, GitLab | Project Management: Jira, Trello, Asana | Communication: Slack, Microsoft Teams, Zoom | Design: Figma, Adobe XD | Testing: Jest, Jasmine, Karma, Cypress | CI/CD: Jenkins, GitHub Actions, GitLab CI | Cloud: AWS, Firebase, Netlify, Vercel.",

    # Education & Learning
    'education': "Jahul Khan has a strong foundation in Computer Science and Web Development. He completed his formal education in Information Technology and has continuously upgraded his skills through online courses, certifications, and hands-on project experience. He believes in lifelong learning and stays updated with the latest Angular versions and frontend technologies.",

    'certifications': "Jahul has completed various professional certifications and courses in: Angular Advanced Concepts, TypeScript Mastery, RxJS and Reactive Programming, NgRx State Management, Frontend Performance Optimization, Web Accessibility (WCAG), Agile and Scrum methodologies, AWS Cloud Fundamentals. He regularly attends webinars, tech conferences, and workshops to stay current.",

    'learning': "Jahul is passionate about continuous learning. Currently exploring: Angular 19 new features and Signals, Micro-frontend architecture, Progressive Web Apps (PWA), Web Components, GraphQL integration, Server-side rendering with Angular Universal, Advanced RxJS patterns, Web performance optimization techniques, Accessibility best practices, Cloud deployment strategies.",

    # Expertise & Specializations
    'specialization': "Jahul specializes in: Enterprise-scale Angular applications, Multi-tenant SaaS platforms, E-commerce solutions, Travel and hospitality tech, Fintech applications, Real-time dashboards and analytics, Complex state management, Performance optimization, White-label solutions, Responsive web design, Progressive Web Apps, Component library development.",

    'expertise': "Core Expertise: Angular 19 architecture and best practices, TypeScript advanced patterns, RxJS reactive programming, NgRx state management, Performance optimization (40% improvement achieved), Responsive design and mobile-first development, RESTful API integration, Component-driven development, Micro-frontend architecture, Testing strategies (unit, integration, e2e), CI/CD implementation, Code review and mentoring.",

    # Soft Skills
    'softskills': "Jahul possesses strong soft skills including: Excellent communication (technical and non-technical), Team leadership and collaboration, Problem-solving and analytical thinking, Time management and prioritization, Attention to detail and quality focus, Adaptability to new technologies, Mentoring and knowledge sharing, Client relationship management, Critical thinking, Creative solution design, Project planning and estimation.",

    'languages': "Languages: English (Fluent - Professional working proficiency), Hindi (Native speaker), Programming Languages: TypeScript, JavaScript, HTML, CSS/SCSS. Comfortable working with international teams across different time zones.",

    # Company & Industry
    'company': "V2F Technology (Visa2Fly) is a leading visa tech company revolutionizing the visa application process. The company provides end-to-end visa solutions for travelers, travel agents, and corporate clients. V2F Technology has partnerships with 24+ major airlines, travel platforms, and fintech companies. The platform has achieved 500,000+ users and maintains a 99.3% visa approval rate.",

    'industry': "Jahul works in the Travel Technology and Fintech sectors, specifically in: Visa and immigration tech, Online travel booking platforms, B2B travel solutions, White-label SaaS platforms, Payment gateway integration, Document processing automation, Customer relationship management, Analytics and reporting systems.",

    # Future Goals
    'goals': "Jahul's professional goals include: Becoming a recognized Angular expert and thought leader, Contributing more to open-source Angular projects, Speaking at international tech conferences, Building his own SaaS product, Mentoring aspiring developers, Writing technical books or courses, Exploring full-stack development with Node.js, Learning cloud architecture (AWS/Azure), Staying at the forefront of frontend technologies.",

    'passion': "Jahul is passionate about: Building beautiful and performant user interfaces, Solving complex technical challenges, Optimizing application performance, Creating exceptional user experiences, Teaching and mentoring others, Open-source contribution, Exploring new technologies, Code quality and best practices, Making web accessible to everyone, Continuous learning and growth.",

    # Hobbies & Interests
    'hobby': "Jahul's hobbies include coding personal projects, learning new technologies and frameworks, contributing to open-source projects, reading tech blogs and documentation, attending tech meetups and conferences, experimenting with new Angular features, mentoring junior developers, and staying updated with web development trends.",
    'hobbies': "Outside of work, Jahul enjoys: Coding side projects to explore new technologies, Contributing to open-source Angular libraries, Reading technical books and blogs, Attending developer meetups and conferences, Learning about new frontend frameworks and tools, Helping other developers through mentoring and code reviews, Experimenting with web performance optimization techniques.",
    'interests': "Jahul is interested in: Angular ecosystem and latest features, Frontend architecture patterns, State management solutions, Performance optimization techniques, Component design systems, Web accessibility (a11y), Progressive Web Apps (PWA), Micro-frontend architectures, TypeScript advanced patterns, Cloud deployment strategies, DevOps for frontend apps.",
}

def find_answer(question):
    """Find best matching answer based on keywords with fuzzy matching"""
    question_lower = question.lower()

    # Remove extra spaces and normalize
    question_normalized = ' '.join(question_lower.split())

    # Personal & About
    if any(word in question_normalized for word in ['who is', 'who are', 'tell me about jahul', 'about jahul', 'introduce']):
        return KNOWLEDGE_BASE['about']
    elif any(word in question_normalized for word in ['bio', 'biography', 'background', 'profile']):
        return KNOWLEDGE_BASE['bio']
    elif any(word in question_normalized for word in ['name', 'called', 'full name']):
        return KNOWLEDGE_BASE['name']

    # Experience & Work
    elif any(word in question_normalized for word in ['experience', 'work history', 'career', 'years']):
        return KNOWLEDGE_BASE['experience']
    elif any(word in question_normalized for word in ['current job', 'current role', 'now working', 'present job', 'current position']):
        return KNOWLEDGE_BASE['current_job']
    elif any(word in question_normalized for word in ['work', 'job', 'employer', 'company']):
        return KNOWLEDGE_BASE['work']
    elif any(word in question_normalized for word in ['responsibility', 'duties', 'role', 'what does he do']):
        return KNOWLEDGE_BASE['responsibilities']

    # Technical Skills
    elif any(word in question_normalized for word in ['skill', 'technology', 'tech stack', 'technologies', 'know']):
        return KNOWLEDGE_BASE['skills']
    elif any(word in question_normalized for word in ['angular', 'framework']):
        return KNOWLEDGE_BASE['angular']
    elif any(word in question_normalized for word in ['typescript', 'ts', 'programming language']):
        return KNOWLEDGE_BASE['typescript']
    elif any(word in question_normalized for word in ['tool', 'software', 'use']):
        return KNOWLEDGE_BASE['tools']
    elif any(word in question_normalized for word in ['expertise', 'expert', 'specialization', 'specialize']):
        return KNOWLEDGE_BASE['expertise']

    # Projects - Visa2Fly with ALL variations
    elif any(pattern in question_normalized for pattern in [
        'visa2fly', 'visa 2 fly', 'visa2fly', 'visa-2-fly', 'visa 2fly', 'visa2 fly',
        'visatofly', 'visa to fly', 'visa fly', 'v2f', 'visa project', 'flagship'
    ]):
        return KNOWLEDGE_BASE['visa2fly']
    elif any(word in question_normalized for word in ['project', 'projects', 'built', 'build', 'developed', 'develop', 'created', 'create', 'portfolio', 'work']):
        return KNOWLEDGE_BASE['projects']

    # White-label - Handle ALL variations and typos
    elif any(pattern in question_normalized for pattern in [
        'white-label', 'white label', 'whitelabel', 'white-lable', 'white lable', 'whitelable',
        'whitelables', 'white-labels', 'white labels', 'whitelabels',
        'wite label', 'wite-label', 'witelabel', 'whit label', 'whit-label',
        'integration', 'partner', 'partners', 'brand', 'brands',
        'indigo', 'spicejet', 'ixigo', 'easemytrip', 'yatra', 'wego', 'cleartrip', 'goibibo',
        'niyo', 'acko', 'hdfc', 'paytm', 'phonepe', 'treebo', 'fabhotel', 'mobikwik'
    ]):
        return KNOWLEDGE_BASE['white-label']

    elif any(word in question_normalized for word in ['b2b', 'vendor', 'portal']):
        return KNOWLEDGE_BASE['b2b_portal']
    elif any(word in question_normalized for word in ['consumer', 'user platform']):
        return KNOWLEDGE_BASE['consumer_platform']

    # Achievements - Handle variations
    elif any(pattern in question_normalized for pattern in [
        'achievement', 'achievements', 'acheivement', 'acheivements',
        'accomplish', 'accomplishment', 'accomplishments',
        'success', 'successful', 'award', 'awards'
    ]):
        return KNOWLEDGE_BASE['achievements']
    elif any(word in question_normalized for word in ['metric', 'metrics', 'number', 'numbers', 'stat', 'stats', 'data', 'how many', 'statistics']):
        return KNOWLEDGE_BASE['metrics']

    # Contact & Social - Handle variations and typos
    elif any(word in question_normalized for word in ['contact', 'reach', 'get in touch', 'hire', 'hiring', 'email', 'mail', 'send message']):
        return KNOWLEDGE_BASE['contact']
    elif any(word in question_normalized for word in ['email', 'mail', 'e-mail', 'gmail', 'send message', 'message']):
        return KNOWLEDGE_BASE['email']

    # LinkedIn - Handle ALL variations
    elif any(pattern in question_normalized for pattern in [
        'linkedin', 'linked in', 'linked-in', 'linkedln', 'linkdin', 'linkd in'
    ]):
        return KNOWLEDGE_BASE['linkedin']

    # GitHub - Handle ALL variations
    elif any(pattern in question_normalized for pattern in [
        'github', 'git hub', 'git-hub', 'githb', 'gthub', 'git', 'code', 'repository', 'repositories', 'repo'
    ]):
        return KNOWLEDGE_BASE['github']

    # Social Media - Handle all platforms
    elif any(pattern in question_normalized for pattern in [
        'social', 'social media', 'facebook', 'fb', 'instagram', 'insta',
        'twitter', 'tweet', 'x.com', 'whatsapp'
    ]):
        return KNOWLEDGE_BASE['social']

    # Location & Availability
    elif any(word in question_lower for word in ['location', 'where', 'based', 'live', 'from']):
        return KNOWLEDGE_BASE['location']
    elif any(word in question_lower for word in ['available', 'hire', 'freelance', 'consulting']):
        return KNOWLEDGE_BASE['available']

    # Education & Learning
    elif any(word in question_lower for word in ['education', 'study', 'degree', 'university']):
        return KNOWLEDGE_BASE['education']
    elif any(word in question_lower for word in ['certification', 'certificate', 'course']):
        return KNOWLEDGE_BASE['certifications']
    elif any(word in question_lower for word in ['learning', 'studying', 'explore']):
        return KNOWLEDGE_BASE['learning']

    # Work Style
    elif any(word in question_lower for word in ['methodology', 'process', 'agile', 'scrum']):
        return KNOWLEDGE_BASE['methodology']
    elif any(word in question_lower for word in ['soft skill', 'communication', 'leadership']):
        return KNOWLEDGE_BASE['softskills']
    elif any(word in question_lower for word in ['language', 'speak', 'english', 'hindi']):
        return KNOWLEDGE_BASE['languages']

    # Company & Industry
    elif any(word in question_lower for word in ['v2f', 'visa2fly company', 'employer']):
        return KNOWLEDGE_BASE['company']
    elif any(word in question_lower for word in ['industry', 'domain', 'sector']):
        return KNOWLEDGE_BASE['industry']

    # Goals & Passion
    elif any(word in question_normalized for word in ['goal', 'future', 'plan', 'aspiration']):
        return KNOWLEDGE_BASE['goals']
    elif any(word in question_normalized for word in ['passion', 'passionate', 'love', 'enjoy']):
        return KNOWLEDGE_BASE['passion']

    # Hobbies & Interests
    elif any(pattern in question_normalized for pattern in [
        'hobby', 'hobbies', 'free time', 'spare time', 'leisure',
        'do for fun', 'outside work', 'when not working'
    ]):
        return KNOWLEDGE_BASE['hobby']
    elif any(word in question_normalized for word in ['hobbies', 'activities', 'pastime']):
        return KNOWLEDGE_BASE['hobbies']
    elif any(word in question_normalized for word in ['interest', 'interests', 'interested']):
        return KNOWLEDGE_BASE['interests']

    # Default response
    else:
        return "I can help you learn about Jahul Khan! I can answer questions about his: Work Experience & Current Role, Technical Skills (Angular, TypeScript, etc.), Projects (Visa2Fly, White-label integrations), Achievements & Metrics, Contact Information (Email, LinkedIn, GitHub), Education & Certifications, Location & Availability, Specializations & Expertise, Goals & Passion, and much more! What would you like to know?"

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
    print("="*80)
    print("🤖 Jahul Khan's AI Chatbot - Comprehensive Knowledge Base")
    print("="*80)
    print(f"📚 Knowledge Categories: {len(KNOWLEDGE_BASE)}")
    print("📋 Topics Covered:")
    print("   • Personal Info & Biography")
    print("   • Work Experience & Current Role")
    print("   • Technical Skills (Angular, TypeScript, RxJS, etc.)")
    print("   • Projects (Visa2Fly, White-label integrations)")
    print("   • Achievements & Metrics (500K+ users, 99.3% approval)")
    print("   • Contact Info (Email, LinkedIn, GitHub)")
    print("   • Education & Certifications")
    print("   • Location & Availability")
    print("   • Expertise & Specializations")
    print("   • Goals, Passion & Future Plans")
    print("")
    print("🚀 Server: http://localhost:5001")
    print("🌐 CORS: Enabled for all origins")
    print("⚡ Matching: Intelligent keyword-based (fast & accurate)")
    print("="*80)
    print("")
    print("Ready to answer questions about Jahul Khan! 🎉")
    print("")
    app.run(debug=True, port=5001, host='0.0.0.0')
