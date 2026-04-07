#!/usr/bin/env python3
"""
Test MongoDB Connection
Verifies MongoDB Atlas connection with your credentials
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import sys

# Your MongoDB credentials
MONGODB_URI = "mongodb+srv://jahulkhan_db_user:cOkS9qN2X7QWTaCE@cluster0.mongodb.net/?retryWrites=true&w=majority"
MONGODB_DB = "jahul_chatbot_prod"

def test_connection():
    """Test MongoDB Atlas connection"""
    print("=" * 80)
    print("🧪 Testing MongoDB Atlas Connection")
    print("=" * 80)
    print()
    
    print("📋 Connection Details:")
    print(f"   URI: mongodb+srv://jahulkhan_db_user:***@cluster0.mongodb.net/")
    print(f"   Database: {MONGODB_DB}")
    print()
    
    try:
        print("🔌 Connecting to MongoDB Atlas...")
        
        client = MongoClient(
            MONGODB_URI,
            serverSelectionTimeoutMS=10000,
            connectTimeoutMS=10000
        )
        
        # Test connection
        print("🔍 Testing connection...")
        client.admin.command('ping')
        
        print("✅ Connection successful!")
        print()
        
        # Get database
        db = client[MONGODB_DB]
        
        # List collections
        print("📊 Database Information:")
        collections = db.list_collection_names()
        print(f"   Collections: {collections if collections else 'None (will be created on first insert)'}")
        print()
        
        # Test insert
        print("📝 Testing insert...")
        test_doc = {
            'test': True,
            'message': 'MongoDB connection test successful!',
            'timestamp': '2024-01-15'
        }
        
        result = db.test_collection.insert_one(test_doc)
        print(f"✅ Insert successful! ID: {result.inserted_id}")
        print()
        
        # Test query
        print("🔍 Testing query...")
        found = db.test_collection.find_one({'test': True})
        if found:
            print(f"✅ Query successful! Found: {found['message']}")
        print()
        
        # Clean up test
        print("🧹 Cleaning up test data...")
        db.test_collection.delete_one({'_id': result.inserted_id})
        print("✅ Cleanup complete")
        print()
        
        # Get stats
        print("📊 Database Statistics:")
        stats = db.command('dbStats')
        print(f"   Database: {stats.get('db', 'N/A')}")
        print(f"   Collections: {stats.get('collections', 0)}")
        print(f"   Data Size: {stats.get('dataSize', 0)} bytes")
        print()
        
        # Close connection
        client.close()
        
        print("=" * 80)
        print("✅ All Tests Passed!")
        print("=" * 80)
        print()
        print("✨ Your MongoDB Atlas is ready to use!")
        print()
        print("Next steps:")
        print("  1. Start backend: cd chatbot-backend && python app_mongodb.py")
        print("  2. Deploy to production: firebase deploy --only functions")
        print()
        
        return True
        
    except ConnectionFailure as e:
        print(f"❌ Connection failed: {e}")
        print()
        print("Troubleshooting:")
        print("  1. Check MongoDB Atlas dashboard")
        print("  2. Verify network access allows 0.0.0.0/0")
        print("  3. Verify database user credentials")
        print("  4. Check if cluster is running")
        return False
        
    except ServerSelectionTimeoutError as e:
        print(f"❌ Server timeout: {e}")
        print()
        print("Troubleshooting:")
        print("  1. Check internet connection")
        print("  2. Verify cluster is not paused")
        print("  3. Check MongoDB Atlas status")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print()
        print(f"Error type: {type(e).__name__}")
        return False

if __name__ == '__main__':
    success = test_connection()
    sys.exit(0 if success else 1)
