"""
Simple test script to verify the chatbot backend is working
Run this AFTER starting the Flask server (python app.py)
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_health():
    """Test health endpoint"""
    print("🔍 Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✅ Health check passed!\n")
            return True
        else:
            print("❌ Health check failed!\n")
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}\n")
        return False

def test_chat():
    """Test chat endpoint"""
    print("🔍 Testing chat endpoint...")
    
    test_questions = [
        "What is your experience?",
        "Tell me about Visa2Fly",
        "What are your skills?"
    ]
    
    for question in test_questions:
        try:
            print(f"\n📤 Question: {question}")
            response = requests.post(
                f"{BASE_URL}/api/chat",
                json={"question": question},
                headers={"Content-Type": "application/json"}
            )
            
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Response: {data['response'][:100]}...")
            else:
                print(f"❌ Error: {response.json()}")
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    print("\n✅ Chat tests completed!\n")

def main():
    print("=" * 60)
    print("🤖 Chatbot Backend Test Script")
    print("=" * 60)
    print()
    
    # Test health endpoint first
    if not test_health():
        print("❌ Backend is not running!")
        print("💡 Start it with: python app.py")
        return
    
    # Test chat endpoint
    test_chat()
    
    print("=" * 60)
    print("🎉 All tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
