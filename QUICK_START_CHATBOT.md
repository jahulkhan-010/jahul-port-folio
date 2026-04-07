# 🚀 Quick Start Guide - AI Chatbot

## Option 1: Run with Python ML Backend (Recommended)

### Step 1: Open a New Terminal

Open a **separate terminal** (don't close your Angular dev server!)

### Step 2: Navigate to Backend Folder

```bash
cd chatbot-backend
```

### Step 3: Create Virtual Environment

```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- sentence-transformers (ML model ~80MB download)
- scikit-learn, numpy, torch

**Note:** First time will take 2-5 minutes to download ML model.

### Step 6: Run the Server

```bash
python app.py
```

You should see:
```
🤖 Starting AI Chatbot Backend...
📚 Knowledge base loaded with 10 entries
🚀 Server running on http://localhost:5000
 * Running on http://127.0.0.1:5000
```

### Step 7: Test the Connection

Open your browser console (F12) and look for:
```
✅ Python ML backend is connected and ready!
```

### Step 8: Test the Chatbot

1. Click the purple chat button in your portfolio
2. Ask a question like "What is Jahul's experience?"
3. You should see the response with "(ML)" tag indicating it's from the ML backend
4. Check the console logs to see the API communication

---

## Option 2: Run Without Python (Fallback Mode)

Just run your Angular app normally:

```bash
npm start
```

The chatbot will automatically use mock responses. You'll see:
```
⚠️ Python backend not available. Using fallback responses.
💡 To enable ML: cd chatbot-backend && ./start.sh
```

Responses will have "(Fallback)" tag.

---

## ✅ How to Know If Python Backend is Connected

### In Browser Console:

**Connected:**
```
✅ Python ML backend is connected and ready!
📤 Sending question to backend: What is your experience?
✅ Received response from Python ML backend: Jahul Khan has 4+ years...
```

**Not Connected:**
```
⚠️ Python backend not available. Using fallback responses.
💡 To enable ML: cd chatbot-backend && ./start.sh
```

### In Chat Messages:

- **(ML)** = Response from Python Machine Learning backend
- **(Fallback)** = Response from Angular mock data

---

## 🔧 Troubleshooting

### "Port 5000 already in use"

Kill the existing process:
```bash
# Find process using port 5000
lsof -i :5000

# Kill it
kill -9 <PID>
```

Or change the port in:
1. `chatbot-backend/app.py` - change `port=5000` to `port=5001`
2. `src/app/components/chatbot/chatbot.component.ts` - change `http://localhost:5000` to `http://localhost:5001`

### "Module not found" errors

Make sure virtual environment is activated:
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

Then reinstall:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### CORS Errors

The Python backend has CORS enabled. If you still see CORS errors:
1. Check that Flask-CORS is installed: `pip install flask-cors`
2. Restart the Python server

### Connection Refused

1. Make sure Python backend is running on http://localhost:5000
2. Check there are no firewall issues
3. Verify the API URL in Angular component matches the Python server

---

## 📊 Test API Directly

Test Python backend without Angular:

```bash
# Health check
curl http://localhost:5000/api/health

# Test chat
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Jahul'\''s experience?"}'
```

Expected response:
```json
{
  "response": "Jahul Khan has 4+ years of professional experience...",
  "status": "success"
}
```

---

## 🎉 Success!

When everything is working:
- ✅ Angular app running on http://localhost:4200 (or another port)
- ✅ Python backend running on http://localhost:5000
- ✅ Chatbot showing "(ML)" responses
- ✅ Console showing Python backend connection

Now you have a fully functional AI-powered chatbot!
