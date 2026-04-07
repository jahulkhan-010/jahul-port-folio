# 🔄 Restart Python Backend - Quick Guide

## ⚡ Quick Restart (Most Common)

If Python backend is already running and you just need to restart it:

### Step 1: Stop Current Backend

In the terminal where Python is running, press:
```
Ctrl + C
```

You'll see:
```
^C
KeyboardInterrupt
```

### Step 2: Restart It

```bash
python app.py
```

**Done!** Wait for:
```
🚀 Server running on http://localhost:5000
```

---

## 🆕 Fresh Start (If Backend Not Running)

If you closed the terminal or backend is not running:

### macOS/Linux:

```bash
cd /Users/jahulkhan/Documents/workspace/personal/jahul-port-folio/chatbot-backend
source venv/bin/activate
python app.py
```

### Windows:

```bash
cd C:\path\to\jahul-port-folio\chatbot-backend
venv\Scripts\activate
python app.py
```

---

## 🔧 Full Reinstall (If Having Issues)

If you're having problems and need to start completely fresh:

```bash
# Navigate to backend folder
cd chatbot-backend

# Remove old virtual environment
rm -rf venv

# Create new virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows

# Install all dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Start the server
python app.py
```

**Note:** First time will download ML model (~80MB), takes 2-5 minutes.

---

## ✅ How to Know It's Working

After running `python app.py`, you should see:

```
🤖 Starting AI Chatbot Backend...
📚 Knowledge base loaded with 10 entries
🚀 Server running on http://localhost:5000
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX
```

**If you see this** → ✅ Backend is running!

---

## 🧪 Quick Test

Test if backend is actually working:

```bash
# In a NEW terminal (keep Python running in the other one)
curl http://localhost:5000/api/health
```

**Should return:**
```json
{
  "cors": "enabled",
  "message": "Chatbot API is running",
  "status": "healthy"
}
```

**If you see this** → ✅ Backend is working perfectly!

---

## 🌐 Test from Angular

1. Open browser: http://localhost:4200
2. Hard refresh: `Ctrl+Shift+R` (or `Cmd+Shift+R` on Mac)
3. Open Console: `F12`
4. Look for:

**✅ Success:**
```
✅ Python ML backend is connected and ready!
```

5. Click chat button
6. Ask: "What is your experience?"
7. Response should end with: `(ML)`

**If you see (ML)** → ✅ Everything is connected!

---

## 🐛 Common Issues

### "Address already in use"

**Problem:** Port 5000 is being used by another process.

**Solution:**
```bash
lsof -i :5000
kill -9 <PID>
```

Then restart: `python app.py`

### "No module named 'flask'"

**Problem:** Virtual environment not activated or dependencies not installed.

**Solution:**
```bash
source venv/bin/activate  # Make sure you see (venv) in prompt
pip install -r requirements.txt
```

### "Command not found: python"

**Problem:** Python not in PATH or using wrong command.

**Try:**
```bash
python3 app.py  # Instead of python app.py
```

### Backend starts but Angular can't connect

**Problem:** CORS or network issue.

**Solution:**
1. Restart Python backend: `Ctrl+C` then `python app.py`
2. Hard refresh Angular: `Ctrl+Shift+R`
3. Check firewall isn't blocking port 5000

---

## 📝 Checklist After Restart

- [ ] Terminal shows "Server running on http://localhost:5000"
- [ ] `curl http://localhost:5000/api/health` works
- [ ] Browser console shows "✅ Python ML backend is connected and ready!"
- [ ] Chat responses show "(ML)" tag
- [ ] No CORS errors in browser console

**All checked?** → **You're all set!** 🎉

---

## 💡 Pro Tips

### Tip 1: Keep Terminal Open
Don't close the terminal where Python is running. Minimize it instead.

### Tip 2: Use Screen/Tmux (Advanced)
For keeping backend running even after closing terminal:
```bash
# Start screen session
screen -S chatbot

# Run backend
cd chatbot-backend
source venv/bin/activate
python app.py

# Detach: Press Ctrl+A then D
# Reattach later: screen -r chatbot
```

### Tip 3: Auto-restart Script
Create `run.sh`:
```bash
#!/bin/bash
cd chatbot-backend
source venv/bin/activate
while true; do
    python app.py
    echo "Backend crashed! Restarting in 5 seconds..."
    sleep 5
done
```

Make executable: `chmod +x run.sh`
Run: `./run.sh`

### Tip 4: Check Backend Status
Quick command to see if backend is running:
```bash
lsof -i :5000 && echo "✅ Backend is running" || echo "❌ Backend is NOT running"
```

---

## 🎯 Most Common Workflow

### Daily Use:

**Morning - Start Backend:**
```bash
cd chatbot-backend
source venv/bin/activate
python app.py
```

**During Day - If Need to Restart:**
```bash
Ctrl+C
python app.py
```

**Evening - Stop Backend:**
```bash
Ctrl+C
deactivate  # Optional: exit virtual environment
```

---

## 🚀 One-Line Restart Command

For maximum efficiency, use this:

```bash
cd chatbot-backend && source venv/bin/activate && python app.py
```

Or create an alias in `~/.bashrc` or `~/.zshrc`:

```bash
alias chatbot='cd /Users/jahulkhan/Documents/workspace/personal/jahul-port-folio/chatbot-backend && source venv/bin/activate && python app.py'
```

Then just type: `chatbot` 🎉

---

**Backend restart complete!** Your AI chatbot is ready to answer questions! 🤖✨
