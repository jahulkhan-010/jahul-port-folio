# 🔌 How to Connect Python Backend to Angular Chatbot

## Current Status

Your chatbot is **working with fallback responses** (mock data). To enable **ML-powered responses**, you need to run the Python backend separately.

---

## Why Mock Data Shows Up

The Angular component is designed to:
1. **Try to connect** to Python backend (http://localhost:5000)
2. **If connection fails** → Use mock responses automatically
3. **Log everything** to console so you can see what's happening

This is a **smart fallback system** - the chatbot works even without Python!

---

## How to Enable Python ML Backend

### Open 2 Terminals:

**Terminal 1: Angular (Already Running)**
```bash
npm start
```
Keep this running!

**Terminal 2: Python Backend (New)**
```bash
cd chatbot-backend
python3 -m venv venv
source venv/bin/activate          # macOS/Linux
pip install -r requirements.txt
python app.py
```

---

## Step-by-Step Process

### 1. Check Current Status

Open browser console (F12) and look for:

```
⚠️ Python backend not available. Using fallback responses.
💡 To enable ML: cd chatbot-backend && ./start.sh
```

This means you're currently using mock data.

### 2. Start Python Backend

In a new terminal:

```bash
cd /Users/jahulkhan/Documents/workspace/personal/jahul-port-folio/chatbot-backend
```

Create virtual environment (first time only):
```bash
python3 -m venv venv
```

Activate it:
```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

Install dependencies (first time only, takes 2-5 mins):
```bash
pip install -r requirements.txt
```

Run the server:
```bash
python app.py
```

### 3. Verify Python is Running

You should see in Terminal 2:

```
🤖 Starting AI Chatbot Backend...
📚 Knowledge base loaded with 10 entries
🚀 Server running on http://localhost:5000
 * Running on http://127.0.0.1:5000
 * Debugmode off
WARNING: This is a development server. Do not use it in a production deployment.
```

### 4. Refresh Angular App

Go back to your browser and **refresh the page**.

Now check browser console - you should see:
```
✅ Python ML backend is connected and ready!
```

### 5. Test the Chatbot

Click the purple chat button and ask:
- "What is Jahul's experience?"
- "Tell me about Visa2Fly"
- "What are your skills?"

**If Python is connected**, response will have **(ML)** tag.
**If using fallback**, response will have **(Fallback)** tag.

---

## Console Logs Explained

### When Python Backend is Connected:

```
✅ Python ML backend is connected and ready!
📤 Sending question to backend: What is your experience?
🔗 API URL: http://localhost:5000/api/chat
✅ Received response from Python ML backend: Jahul Khan has 4+ years...
```

### When Python Backend is NOT Running:

```
⚠️ Python backend not available. Using fallback responses.
📤 Sending question to backend: What is your experience?
🔗 API URL: http://localhost:5000/api/chat
⚠️ Python backend not available, using fallback responses
Error details: HttpErrorResponse {status: 0, message: "..."}
💡 To enable ML: cd chatbot-backend && ./start.sh
```

---

## Visual Indicators

### In Chat Messages:

```
User: What is your experience?
Bot: Jahul has 4+ years of experience... (ML)  ← Python ML Backend
```

```
User: What is your experience?
Bot: Jahul has 4+ years of experience... (Fallback)  ← Mock Data
```

---

## Quick Test Commands

### Test Python Backend Directly:

```bash
# Health check
curl http://localhost:5000/api/health

# Should return:
# {"message":"Chatbot API is running","status":"healthy"}
```

```bash
# Test chat endpoint
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What is your experience?"}'

# Should return JSON with response from ML model
```

---

## Common Issues & Solutions

### Issue 1: "Connection Refused"
**Solution:** Python backend is not running. Follow step 2 above.

### Issue 2: "Port 5000 already in use"
**Solution:** 
```bash
lsof -i :5000
kill -9 <PID>
```

### Issue 3: "Module not found"
**Solution:** Virtual environment not activated or dependencies not installed
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue 4: Still showing "Fallback" responses
**Solution:**
1. Check Python backend is running (Terminal 2)
2. Refresh Angular app (browser)
3. Check browser console for connection logs
4. Verify http://localhost:5000/api/health works

---

## File Locations

```
jahul-port-folio/
├── src/app/components/chatbot/
│   ├── chatbot.component.ts      ← Angular component (Frontend)
│   ├── chatbot.component.html
│   └── chatbot.component.scss
│
└── chatbot-backend/
    ├── app.py                     ← Python Flask API (Backend)
    ├── requirements.txt           ← Python dependencies
    └── start.sh                   ← Quick start script
```

---

## What Happens When You Ask a Question

1. **User types question** → Angular component
2. **Component sends HTTP POST** → http://localhost:5000/api/chat
3. **Python receives request** → Processes with ML model
4. **ML model finds best answer** → Using semantic similarity
5. **Python sends response** → Back to Angular
6. **Angular displays answer** → With "(ML)" tag

If step 2 fails (Python not running) → Skip to fallback → Show mock response with "(Fallback)" tag

---

## Summary

✅ **Currently**: Chatbot works with mock data (automatic fallback)
✅ **To enable ML**: Run Python backend in separate terminal
✅ **How to check**: Look for "(ML)" vs "(Fallback)" tags in responses
✅ **Console logs**: Show exactly what's happening

The chatbot is smart - it always works, whether Python is running or not!
