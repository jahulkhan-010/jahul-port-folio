# 🤖 AI Chatbot Setup Guide

Your portfolio now has an AI-powered chatbot that can answer questions about your experience, skills, and projects!

## ✨ Features

- **Floating Chat Button**: Appears on all pages with a purple gradient design
- **Smart AI Responses**: Uses ML (Sentence Transformers) to understand and answer questions
- **Semantic Search**: Finds the most relevant answers based on meaning, not just keywords
- **Smooth Animations**: Professional chat interface with typing indicators
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Fallback Mode**: Works even without Python backend using mock responses

## 🎯 What the Chatbot Can Answer

The AI assistant can answer questions about:
- **Work Experience**: Current role, previous positions, career timeline
- **Technical Skills**: Angular, TypeScript, frameworks, tools, methodologies
- **Projects**: Visa2Fly platform, white-label integrations, achievements
- **Contact Information**: Email, LinkedIn, GitHub, portfolio
- **Achievements**: User metrics, approval rates, performance improvements
- **And much more!**

## 🚀 Quick Start

### Option 1: Run with Python ML Backend (Recommended)

**Step 1: Set up Python Backend**
```bash
cd chatbot-backend
chmod +x start.sh
./start.sh
```

This will:
- Create a virtual environment
- Install all dependencies (Flask, sentence-transformers, etc.)
- Start the server on http://localhost:5000

**Step 2: Run Angular Frontend**
```bash
# In a new terminal
npm start
```

The chatbot will now use the AI backend for intelligent responses!

### Option 2: Run Without Python Backend (Fallback Mode)

Just run the Angular app:
```bash
npm start
```

The chatbot will automatically use mock responses if the Python backend is not available.

## 📁 Project Structure

```
jahul-port-folio/
├── src/app/components/chatbot/          # Angular chatbot component
│   ├── chatbot.component.ts             # Component logic
│   ├── chatbot.component.html           # Chat UI
│   └── chatbot.component.scss           # Styles
│
└── chatbot-backend/                     # Python ML backend
    ├── app.py                           # Flask API with ML model
    ├── requirements.txt                 # Python dependencies
    ├── start.sh                         # Setup & start script
    └── README.md                        # Backend documentation
```

## 🎨 UI Features

**Floating Chat Button:**
- Fixed position at bottom-right corner
- Purple gradient with hover effects
- Transforms to close button when chat is open

**Chat Modal:**
- 380px width on desktop, full-width on mobile
- Purple-themed header with bot avatar
- Scrollable message area
- Input field with send button
- Typing indicator animation

**Messages:**
- User messages: Right-aligned with purple gradient background
- Bot messages: Left-aligned with bordered card design
- Timestamps for each message
- Smooth slide-in animations

## 🔧 Customization

### Update Knowledge Base

Edit `chatbot-backend/app.py` and modify the `KNOWLEDGE_BASE` array:

```python
{
    "category": "your_topic",
    "question": "What is your question?",
    "answer": "Your detailed answer here..."
}
```

### Change API URL

Edit `src/app/components/chatbot/chatbot.component.ts`:

```typescript
private apiUrl = 'http://localhost:5000/api/chat';
// Change to your production URL
```

### Customize Appearance

Edit `src/app/components/chatbot/chatbot.component.scss` to change:
- Colors (search for `var(--accent-color)`)
- Sizes (chat width, button size, etc.)
- Animations (typing indicator, message slide-in, etc.)

## 🧪 Testing the Chatbot

Try asking these questions:
- "What is Jahul's experience?"
- "Tell me about Visa2Fly project"
- "What skills does Jahul have?"
- "How can I contact Jahul?"
- "What are Jahul's achievements?"
- "What white-label integrations has he done?"

## 🌐 Deployment

### Deploy Angular Frontend
- Build: `npm run build`
- Deploy `dist/` folder to your hosting service

### Deploy Python Backend
Options:
1. **Heroku**: `git push heroku main`
2. **AWS Lambda**: Use Zappa or Serverless framework
3. **Google Cloud Run**: Containerize with Docker
4. **Railway/Render**: Direct deployment from Git

Don't forget to update the API URL in the Angular component!

## 📊 Technical Details

**Frontend:**
- Angular 19 (Standalone Components)
- HttpClient for API calls
- Reactive Forms
- SCSS animations

**Backend:**
- Flask (Python web framework)
- sentence-transformers (for ML-based semantic search)
- scikit-learn (cosine similarity)
- CORS enabled for cross-origin requests

**ML Model:**
- Model: `all-MiniLM-L6-v2`
- Size: ~80MB
- Speed: ~50ms per query
- Accuracy: High semantic understanding

## 🎉 Result

Your portfolio now has an intelligent AI assistant that can:
✅ Answer questions 24/7
✅ Understand natural language
✅ Provide accurate information about your work
✅ Improve user engagement
✅ Showcase your technical skills

## 📝 Notes

- First run of Python backend will download the ML model (~80MB)
- Chatbot works offline with fallback responses
- Mobile responsive and accessible
- No API keys or external services required
