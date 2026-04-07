#!/usr/bin/env python3
"""
Admin Panel for AI Learning Chatbot
View, manage, and train the chatbot with custom Q&A pairs
"""

import json
import os
from datetime import datetime

CONVERSATIONS_FILE = 'conversations_history.json'

def load_conversations():
    """Load all conversations"""
    if os.path.exists(CONVERSATIONS_FILE):
        with open(CONVERSATIONS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_conversations(conversations):
    """Save conversations"""
    with open(CONVERSATIONS_FILE, 'w') as f:
        json.dump(conversations, f, indent=2)

def view_all_conversations():
    """View all learned conversations"""
    conversations = load_conversations()
    if not conversations:
        print("📭 No conversations learned yet!")
        return
    
    print(f"\n📚 Total Conversations: {len(conversations)}")
    print("="*80)
    
    for i, conv in enumerate(conversations, 1):
        print(f"\n#{i}")
        print(f"❓ Q: {conv['question']}")
        print(f"💬 A: {conv['answer'][:100]}{'...' if len(conv['answer']) > 100 else ''}")
        print(f"🏷️  Source: {conv['source']}")
        print(f"📅 Time: {conv['timestamp']}")
        print("-"*80)

def add_custom_qa():
    """Add custom Q&A pair"""
    print("\n➕ Add Custom Q&A Pair")
    print("="*80)
    
    question = input("Enter Question: ").strip()
    if not question:
        print("❌ Question cannot be empty!")
        return
    
    answer = input("Enter Answer: ").strip()
    if not answer:
        print("❌ Answer cannot be empty!")
        return
    
    conversations = load_conversations()
    conversations.append({
        'question': question,
        'answer': answer,
        'source': 'admin_added',
        'timestamp': datetime.now().isoformat(),
        'question_lower': question.lower().strip()
    })
    
    save_conversations(conversations)
    print(f"✅ Added successfully! Total: {len(conversations)}")

def search_conversations():
    """Search conversations by keyword"""
    keyword = input("\n🔍 Enter search keyword: ").strip().lower()
    if not keyword:
        return
    
    conversations = load_conversations()
    matches = [c for c in conversations if keyword in c['question_lower'] or keyword in c['answer'].lower()]
    
    if not matches:
        print(f"❌ No matches found for '{keyword}'")
        return
    
    print(f"\n✅ Found {len(matches)} matches:")
    print("="*80)
    
    for i, conv in enumerate(matches, 1):
        print(f"\n#{i}")
        print(f"❓ Q: {conv['question']}")
        print(f"💬 A: {conv['answer'][:100]}{'...' if len(conv['answer']) > 100 else ''}")
        print("-"*80)

def clear_all_conversations():
    """Clear all learned conversations"""
    confirm = input("\n⚠️  Clear ALL conversations? (yes/no): ").strip().lower()
    if confirm == 'yes':
        save_conversations([])
        print("✅ All conversations cleared!")
    else:
        print("❌ Cancelled")

def export_conversations():
    """Export conversations to readable format"""
    conversations = load_conversations()
    filename = f"conversations_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(filename, 'w') as f:
        f.write(f"Chatbot Conversations Export\n")
        f.write(f"Total: {len(conversations)}\n")
        f.write(f"Exported: {datetime.now()}\n")
        f.write("="*80 + "\n\n")
        
        for i, conv in enumerate(conversations, 1):
            f.write(f"#{i}\n")
            f.write(f"Question: {conv['question']}\n")
            f.write(f"Answer: {conv['answer']}\n")
            f.write(f"Source: {conv['source']}\n")
            f.write(f"Time: {conv['timestamp']}\n")
            f.write("-"*80 + "\n\n")
    
    print(f"✅ Exported to: {filename}")

def show_stats():
    """Show learning statistics"""
    conversations = load_conversations()
    
    if not conversations:
        print("📊 No data yet!")
        return
    
    unique_questions = set(c['question_lower'] for c in conversations)
    sources = {}
    for c in conversations:
        sources[c['source']] = sources.get(c['source'], 0) + 1
    
    print("\n📊 Learning Statistics")
    print("="*80)
    print(f"Total Conversations: {len(conversations)}")
    print(f"Unique Questions: {len(unique_questions)}")
    print(f"\nBy Source:")
    for source, count in sources.items():
        print(f"  • {source}: {count}")
    print("="*80)

def main_menu():
    """Main menu"""
    while True:
        print("\n" + "="*80)
        print("🧠 AI Learning Chatbot - Admin Panel")
        print("="*80)
        print("1. View All Conversations")
        print("2. Add Custom Q&A Pair")
        print("3. Search Conversations")
        print("4. Show Statistics")
        print("5. Export Conversations")
        print("6. Clear All Conversations")
        print("7. Exit")
        print("="*80)
        
        choice = input("Choose option (1-7): ").strip()
        
        if choice == '1':
            view_all_conversations()
        elif choice == '2':
            add_custom_qa()
        elif choice == '3':
            search_conversations()
        elif choice == '4':
            show_stats()
        elif choice == '5':
            export_conversations()
        elif choice == '6':
            clear_all_conversations()
        elif choice == '7':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid option!")

if __name__ == '__main__':
    main_menu()
