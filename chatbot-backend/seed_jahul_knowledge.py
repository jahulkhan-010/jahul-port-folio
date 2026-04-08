#!/usr/bin/env python3
"""
Seed MongoDB with Jahul Khan's knowledge base
Run this to populate initial data
"""

import os
os.environ['ENVIRONMENT'] = os.getenv('ENVIRONMENT', 'atlas')

from mongodb_client import mongodb_client

# Comprehensive knowledge about Jahul Khan
JAHUL_KNOWLEDGE = [
    # Personal & Introduction
    {
        "question": "Who is Jahul Khan?",
        "answer": "Jahul Khan is a Senior Frontend Developer with 4+ years of professional experience specializing in Angular development. Currently at V2F Technology, he leads the Visa2Fly platform development serving 500,000+ users with 99.3% visa approval rate."
    },
    {
        "question": "Tell me about Jahul",
        "answer": "Jahul Khan is a passionate Senior Frontend Developer with expertise in Angular 19, TypeScript, and modern web technologies. He has successfully delivered enterprise-scale applications with 500K+ users and 24+ white-label integrations."
    },
    
    # Experience
    {
        "question": "What is your experience?",
        "answer": "Jahul has 4+ years of professional experience as a Senior Frontend Developer at V2F Technology (May 2023-Present), Angular Developer at IMG Global Infotech (May 2022-May 2023), and Angular Intern at Success Ladder Technologies (Feb 2022-May 2022)."
    },
    {
        "question": "What is your current job?",
        "answer": "Currently working as Senior Frontend Developer at V2F Technology since May 2023, leading the development of Visa2Fly platform serving 500,000+ users with 99.3% visa approval rate across 50+ countries."
    },
    
    # Skills
    {
        "question": "What are your skills?",
        "answer": "Expert in Angular 19, TypeScript, JavaScript ES6+, HTML5, CSS3/SCSS, RxJS, NgRx state management, Material Design, PrimeNG, Bootstrap, Tailwind CSS, Git, RESTful APIs, MongoDB, Firebase, Jest/Jasmine testing."
    },
    {
        "question": "Do you know Angular?",
        "answer": "Yes! Jahul has deep expertise in Angular 19 with skills in: Component architecture, Dependency injection, RxJS operators, NgRx state management, Angular Router, Reactive & Template-driven Forms, HTTP Client, Material Design, Lazy loading, Standalone components, Signals, and Performance optimization."
    },
    {
        "question": "Do you know TypeScript?",
        "answer": "Yes! Jahul has advanced TypeScript skills including: Strong typing, Generics, Decorators, OOP patterns, Type guards, Enums, Async/await, ES6+ features, and advanced type inference."
    },
    
    # Projects
    {
        "question": "Tell me about Visa2Fly",
        "answer": "Visa2Fly is Jahul's flagship project - a comprehensive visa application platform with 500,000+ users, 99.3% approval rate, supporting 50+ countries. Features include AI-powered document validation, real-time tracking, payment integration, multi-language support, and 24+ white-label partner integrations."
    },
    {
        "question": "What projects have you built?",
        "answer": "Major projects: (1) Visa2Fly Ecosystem - 4 enterprise applications (Consumer, B2B, Agent, Admin), (2) 24+ White-label integrations with airlines and travel platforms, (3) B2B Vendor Portal for travel agents, (4) Agent Dashboard with analytics, (5) Admin Analytics Platform. All built with Angular 19, TypeScript, and NgRx."
    },
    {
        "question": "What are white-label integrations?",
        "answer": "Jahul has successfully integrated Visa2Fly with 24+ leading brands: Airlines (IndiGo, SpiceJet, Vistara, Air India Express, AirAsia), Travel Platforms (ixigo, EaseMyTrip, Yatra, Wego, Cleartrip, Goibibo), Fintech (Niyo, ACKO Insurance, HDFC SmartBuy, Paytm, PhonePe), Hotels (Treebo, FabHotels), and others (Mobikwik, Amazon Pay, Google Pay). Built with multi-tenant architecture and custom theming."
    },
    
    # Achievements
    {
        "question": "What are your achievements?",
        "answer": "Key achievements: Served 500,000+ users, achieved 99.3% visa approval rate, delivered 24+ white-label partner integrations, built 4 enterprise applications, improved performance by 40%, reduced page load times by 60%, decreased bugs by 35%, maintained 95%+ code coverage, zero critical production bugs, and mentored 5+ junior developers."
    },
    {
        "question": "How many users?",
        "answer": "The Visa2Fly platform serves 500,000+ total users with 1000+ daily active users and processes 10,000+ visa applications monthly across 50+ countries."
    },
    
    # Contact
    {
        "question": "How can I contact you?",
        "answer": "Contact Jahul at: Professional Email - jahul.khan@visa2fly.com, Personal Email - jahulkhan010@gmail.com, LinkedIn - search 'Jahul Khan', GitHub - active repositories available, Portfolio - jahulkhan.dev. Based in India, available for remote work worldwide."
    },
    {
        "question": "What is your email?",
        "answer": "Professional: jahul.khan@visa2fly.com | Personal: jahulkhan010@gmail.com"
    },
    {
        "question": "Where can I find you on LinkedIn?",
        "answer": "Find Jahul Khan on LinkedIn for professional profile, endorsements, recommendations, project details, and latest updates. Active in professional networking and industry insights."
    },
    {
        "question": "What is your GitHub?",
        "answer": "Jahul maintains an active GitHub profile with Angular projects, TypeScript utilities, UI component libraries, and code samples demonstrating clean code practices and modern development patterns."
    },
    
    # Personal
    {
        "question": "What are your hobbies?",
        "answer": "Jahul's hobbies include coding personal projects, learning new technologies and frameworks, contributing to open-source projects, reading tech blogs and documentation, attending tech meetups and conferences, experimenting with new Angular features, and mentoring junior developers."
    },
    {
        "question": "What is your hobby?",
        "answer": "Jahul enjoys coding personal projects, learning new technologies, contributing to open-source, attending tech meetups, experimenting with Angular, and mentoring developers."
    },
    {
        "question": "What are you passionate about?",
        "answer": "Passionate about building beautiful user interfaces, solving complex technical challenges, optimizing application performance, creating exceptional user experiences, teaching and mentoring others, contributing to open-source, exploring cutting-edge technologies, code quality, web accessibility, and continuous learning."
    },
    
    # Location & Availability
    {
        "question": "Where are you based?",
        "answer": "Based in India, works with international clients across different time zones. Experienced in remote collaboration using Slack, Teams, Zoom. Follows Agile/Scrum methodologies."
    },
    {
        "question": "Are you available for freelance?",
        "answer": "Currently employed at V2F Technology, open to: Freelance Angular projects, technical consulting, code review services, mentoring, part-time consulting work, speaking at tech events, and technical writing."
    },
    
    # Goals
    {
        "question": "What are your goals?",
        "answer": "Professional goals: Become a recognized Angular expert, contribute to open-source Angular projects, speak at international tech conferences, build own SaaS product, mentor aspiring developers, write technical content, explore full-stack development with Node.js, and master cloud architecture."
    },
]

def seed_database():
    """Seed MongoDB with Jahul's knowledge"""
    
    if not mongodb_client.connected:
        print("❌ MongoDB is not connected!")
        print("Please check your .env configuration")
        return
    
    print("\n" + "="*80)
    print("🌱 Seeding MongoDB with Jahul Khan's Knowledge Base")
    print("="*80)
    print("")
    
    # Check if data already exists
    existing_count = mongodb_client.db.chat_bot_collection.count_documents({})
    
    if existing_count > 0:
        print(f"⚠️  Database already has {existing_count} entries")
        confirm = input("Do you want to add more data? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("❌ Cancelled")
            return
    
    print(f"📝 Adding {len(JAHUL_KNOWLEDGE)} knowledge entries...")
    print("")
    
    added = 0
    skipped = 0
    
    for item in JAHUL_KNOWLEDGE:
        # Check if already exists
        existing = mongodb_client.db.chat_bot_collection.find_one({
            'question_lower': item['question'].lower()
        })
        
        if existing:
            print(f"⏭️  Skipped (exists): {item['question'][:50]}...")
            skipped += 1
            continue
        
        # Save to MongoDB
        saved = mongodb_client.save_conversation(
            question=item['question'],
            answer=item['answer'],
            source='seed_data'
        )
        
        if saved:
            print(f"✅ Added: {item['question'][:50]}...")
            added += 1
        else:
            print(f"❌ Failed: {item['question'][:50]}...")
    
    print("")
    print("="*80)
    print(f"✅ Seeding Complete!")
    print("="*80)
    print(f"Added: {added}")
    print(f"Skipped: {skipped}")
    print(f"Total in DB: {mongodb_client.db.chat_bot_collection.count_documents({})}")
    print("")
    print("🎉 Knowledge base is ready!")
    print("")

if __name__ == '__main__':
    seed_database()
