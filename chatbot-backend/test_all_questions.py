#!/usr/bin/env python3
"""
Test all chatbot questions to ensure proper responses
"""

import requests
import json

API_URL = "http://localhost:5001/api/chat"

# Comprehensive test questions
TEST_QUESTIONS = {
    "Personal & About": [
        "Who is Jahul Khan?",
        "Tell me about Jahul",
        "What's his background?",
    ],
    "Experience & Work": [
        "What is your experience?",
        "What's his work history?",
        "What's his current job?",
        "What does he do?",
    ],
    "Skills": [
        "What are his skills?",
        "What technologies does he know?",
        "Tell me about Angular",
        "Does he know TypeScript?",
    ],
    "Projects": [
        "Tell me about Visa2Fly",
        "What projects has he built?",
        "What white-label integrations?",
        "Tell me about the B2B portal",
    ],
    "Achievements": [
        "What are his achievements?",
        "What metrics has he achieved?",
        "How many users?",
    ],
    "Contact & Social": [
        "How can I contact him?",
        "What's his email?",
        "Where is he on LinkedIn?",
        "What's his GitHub?",
    ],
    "Hobbies & Interests": [
        "What's Jahul's hobby?",
        "What are his hobbies?",
        "What does he do for fun?",
        "What are his interests?",
    ],
    "Location & Availability": [
        "Where is he based?",
        "Is he available for freelance?",
    ],
    "Goals & Passion": [
        "What are his goals?",
        "What is he passionate about?",
    ],
}

def test_question(question):
    """Test a single question"""
    try:
        response = requests.post(API_URL, json={"question": question}, timeout=5)
        if response.status_code == 200:
            data = response.json()
            answer = data.get('response', '')
            
            # Check if it's a generic/fallback response
            is_generic = "I can help you learn about Jahul Khan" in answer or "What would you like to know?" in answer
            
            return {
                'success': True,
                'is_generic': is_generic,
                'answer': answer[:100] + "..." if len(answer) > 100 else answer
            }
        else:
            return {'success': False, 'error': f"HTTP {response.status_code}"}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def main():
    print("=" * 80)
    print("🧪 Testing All Chatbot Questions")
    print("=" * 80)
    print()
    
    # Check if backend is running
    try:
        health = requests.get("http://localhost:5001/api/health", timeout=5)
        if health.status_code != 200:
            print("❌ Backend not running! Start with: python app.py")
            return
    except:
        print("❌ Backend not running! Start with: python app.py")
        return
    
    print("✅ Backend is running")
    print()
    
    total_tests = 0
    passed_tests = 0
    generic_responses = 0
    failed_tests = 0
    
    for category, questions in TEST_QUESTIONS.items():
        print(f"\n📋 {category}")
        print("-" * 80)
        
        for question in questions:
            total_tests += 1
            result = test_question(question)
            
            if result['success']:
                if result['is_generic']:
                    print(f"⚠️  {question}")
                    print(f"    Generic response (needs improvement)")
                    generic_responses += 1
                else:
                    print(f"✅ {question}")
                    print(f"    {result['answer']}")
                    passed_tests += 1
            else:
                print(f"❌ {question}")
                print(f"    Error: {result['error']}")
                failed_tests += 1
    
    # Summary
    print()
    print("=" * 80)
    print("📊 Test Summary")
    print("=" * 80)
    print(f"Total Tests:      {total_tests}")
    print(f"✅ Passed:        {passed_tests} ({passed_tests/total_tests*100:.1f}%)")
    print(f"⚠️  Generic:       {generic_responses} ({generic_responses/total_tests*100:.1f}%)")
    print(f"❌ Failed:        {failed_tests} ({failed_tests/total_tests*100:.1f}%)")
    print("=" * 80)
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! Chatbot is working perfectly!")
    elif generic_responses > 0:
        print("⚠️  Some questions getting generic responses. Check pattern matching.")
    elif failed_tests > 0:
        print("❌ Some tests failed. Check backend logs.")

if __name__ == '__main__':
    main()
