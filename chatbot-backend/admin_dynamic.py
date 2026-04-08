#!/usr/bin/env python3
"""
Dynamic AI Chatbot - Admin Panel
Manage MongoDB knowledge base
"""

import os
os.environ['ENVIRONMENT'] = os.getenv('ENVIRONMENT', 'atlas')

from mongodb_client import mongodb_client
from datetime import datetime

def view_all_knowledge():
    """View all learned knowledge"""
    try:
        conversations = list(mongodb_client.db.chat_bot_collection.find().sort('timestamp', -1).limit(50))
        
        if not conversations:
            print("\n📭 Knowledge base is empty!")
            print("💡 Start chatting to build the knowledge base.")
            return
        
        print(f"\n📚 Knowledge Base ({len(conversations)} most recent entries)")
        print("="*80)
        
        for i, conv in enumerate(conversations, 1):
            print(f"\n#{i}")
            print(f"❓ Question: {conv.get('question', 'N/A')}")
            print(f"💬 Answer: {conv.get('answer', 'N/A')[:150]}{'...' if len(conv.get('answer', '')) > 150 else ''}")
            print(f"🏷️  Source: {conv.get('source', 'N/A')}")
            print(f"📅 Time: {conv.get('timestamp', 'N/A')}")
            print("-"*80)
    
    except Exception as e:
        print(f"❌ Error: {e}")

def add_knowledge():
    """Add new knowledge"""
    print("\n➕ Add New Knowledge")
    print("="*80)
    
    question = input("Enter Question: ").strip()
    if not question:
        print("❌ Question cannot be empty!")
        return
    
    answer = input("Enter Answer: ").strip()
    if not answer:
        print("❌ Answer cannot be empty!")
        return
    
    # Save to MongoDB
    saved = mongodb_client.save_conversation(
        question=question,
        answer=answer,
        source='admin_added'
    )
    
    if saved:
        stats = mongodb_client.get_stats()
        print(f"\n✅ Knowledge added successfully!")
        print(f"📊 Total in knowledge base: {stats.get('total_conversations', 0)}")
    else:
        print(f"\n❌ Failed to add knowledge")

def search_knowledge():
    """Search knowledge base"""
    keyword = input("\n🔍 Enter search keyword: ").strip()
    
    if not keyword:
        return
    
    try:
        results = mongodb_client.search_by_keywords([keyword])
        
        if not results:
            print(f"\n❌ No results found for '{keyword}'")
            return
        
        print(f"\n✅ Found {len(results)} results:")
        print("="*80)
        
        for i, result in enumerate(results, 1):
            print(f"\n#{i}")
            print(f"❓ Q: {result.get('question', 'N/A')}")
            print(f"💬 A: {result.get('answer', 'N/A')[:150]}...")
            print("-"*80)
    
    except Exception as e:
        print(f"❌ Error: {e}")

def bulk_import():
    """Bulk import knowledge from JSON file"""
    print("\n📥 Bulk Import Knowledge")
    print("="*80)
    
    filename = input("Enter JSON filename (or press Enter for default 'knowledge.json'): ").strip()
    if not filename:
        filename = 'knowledge.json'
    
    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        return
    
    try:
        import json
        with open(filename, 'r') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            print("❌ JSON must be a list of {question, answer} objects")
            return
        
        imported = 0
        for item in data:
            if 'question' in item and 'answer' in item:
                saved = mongodb_client.save_conversation(
                    question=item['question'],
                    answer=item['answer'],
                    source='bulk_import'
                )
                if saved:
                    imported += 1
        
        print(f"\n✅ Imported {imported} entries!")
        stats = mongodb_client.get_stats()
        print(f"📊 Total in knowledge base: {stats.get('total_conversations', 0)}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

def export_knowledge():
    """Export all knowledge to JSON"""
    print("\n📤 Export Knowledge Base")
    print("="*80")

    filename = f"knowledge_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    try:
        import json

        conversations = list(mongodb_client.db.chat_bot_collection.find())
        
        # Convert to JSON-serializable format
        export_data = []
        for conv in conversations:
            export_data.append({
                'question': conv.get('question', ''),
                'answer': conv.get('answer', ''),
                'source': conv.get('source', ''),
                'timestamp': str(conv.get('timestamp', ''))
            })
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        print(f"✅ Exported {len(export_data)} entries to: {filename}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

def clear_knowledge():
    """Clear all knowledge (dangerous!)"""
    print("\n⚠️  CLEAR ALL KNOWLEDGE")
    print("="*80)
    print("This will DELETE ALL learned knowledge from the database!")
    confirm = input("Type 'DELETE ALL' to confirm: ").strip()

    if confirm == 'DELETE ALL':
        try:
            result = mongodb_client.db.chat_bot_collection.delete_many({})
            print(f"\n✅ Deleted {result.deleted_count} entries")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print("❌ Cancelled")

def show_stats():
    """Show statistics"""
    stats = mongodb_client.get_stats()
    
    print("\n📊 Knowledge Base Statistics")
    print("="*80)
    print(f"Total Conversations: {stats.get('total_conversations', 0)}")
    print(f"Database Status: {'✅ Connected' if stats.get('connected') else '❌ Disconnected'}")
    print(f"Environment: {stats.get('environment', 'N/A')}")
    
    # Get source breakdown
    try:
        sources = mongodb_client.db.chat_bot_collection.aggregate([
            {'$group': {'_id': '$source', 'count': {'$sum': 1}}}
        ])
        
        print(f"\nBy Source:")
        for source in sources:
            print(f"  • {source['_id']}: {source['count']}")
    except:
        pass
    
    print("="*80)

def main_menu():
    """Main menu"""
    
    if not mongodb_client.connected:
        print("\n❌ MongoDB is not connected!")
        print("Please check your connection settings in .env file")
        return
    
    while True:
        print("\n" + "="*80)
        print("🧠 DYNAMIC AI CHATBOT - Admin Panel")
        print("="*80)
        print("1. View All Knowledge")
        print("2. Add New Knowledge")
        print("3. Search Knowledge")
        print("4. Show Statistics")
        print("5. Bulk Import (JSON)")
        print("6. Export Knowledge")
        print("7. Clear All Knowledge")
        print("8. Exit")
        print("="*80)
        
        choice = input("Choose option (1-8): ").strip()
        
        if choice == '1':
            view_all_knowledge()
        elif choice == '2':
            add_knowledge()
        elif choice == '3':
            search_knowledge()
        elif choice == '4':
            show_stats()
        elif choice == '5':
            bulk_import()
        elif choice == '6':
            export_knowledge()
        elif choice == '7':
            clear_knowledge()
        elif choice == '8':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid option!")

if __name__ == '__main__':
    main_menu()
