# 🚀 Run Both Services with ONE Command

## ✨ Single Command to Start Everything!

I've created **ONE simple command** that:
- ✅ Starts Python ML backend (http://localhost:5000)
- ✅ Starts Angular frontend (http://localhost:4200)
- ✅ Auto-opens browser
- ✅ Monitors both services
- ✅ Stops both with Ctrl+C

---

## 🎯 THE ONE COMMAND:

### **macOS/Linux:**

```bash
./start.sh
```

That's it! Just **one command**! 🎉

---

## 📋 First Time Setup (Only Once)

If this is your first time, run these commands first:

```bash
# Make the script executable
chmod +x start.sh

# Setup Python virtual environment
cd chatbot-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Install npm dependencies
npm install
```

**Then run:**
```bash
./start.sh
```

---

## 🌐 What Happens When You Run It

**You'll see:**
```
═══════════════════════════════════════════════════════════
   🚀 Jahul's Portfolio + AI Chatbot Launcher 🤖
═══════════════════════════════════════════════════════════

[1/2] Starting Python ML Backend...
─────────────────────────────────────────────────────────
🤖 Starting Python on http://localhost:5000
✅ Python backend running (PID: 12345)

[2/2] Starting Angular Frontend...
─────────────────────────────────────────────────────────
⚡ Starting Angular on http://localhost:4200
✅ Angular frontend running (PID: 12346)

═══════════════════════════════════════════════════════════
   🎉 ALL SERVICES RUNNING!
═══════════════════════════════════════════════════════════

📊 Services:
   Python Backend:  http://localhost:5000
   Angular App:     http://localhost:4200

🌐 Open in browser:
   http://localhost:4200

💬 Test AI Chatbot:
   1. Click purple chat button (bottom-right)
   2. Ask: 'What is your experience?'
   3. Response should show (ML) tag

⏹️  Stop services:
   Press Ctrl+C in this terminal

═══════════════════════════════════════════════════════════

🌐 Opening browser...

Monitoring services... (Press Ctrl+C to stop)
```

**Browser will auto-open at:** http://localhost:4200

---

## 🎨 Alternative Methods

### Method 1: Using start.sh (Recommended)
```bash
./start.sh
```
**Features:**
- Auto-opens browser
- Monitors both services
- Clean shutdown with Ctrl+C
- Colored output

### Method 2: Using npm
```bash
npm run dev
```
**Features:**
- Shows both outputs in same terminal
- Color-coded prefixes

### Method 3: Using start-all.sh
```bash
./start-all.sh
```
**Features:**
- Runs in background
- Creates log files

---

## 📊 URLs After Starting

| Service | URL | Description |
|---------|-----|-------------|
| **Portfolio Website** | http://localhost:4200 | Main Angular app |
| **Python API Health** | http://localhost:5000/api/health | Health check |
| **Python API Chat** | http://localhost:5000/api/chat | Chat endpoint (POST) |

---

## ✅ Verify Everything is Working

### Step 1: Check Terminal Output

You should see:
```
✅ Python backend running (PID: 12345)
✅ Angular frontend running (PID: 12346)
🎉 ALL SERVICES RUNNING!
```

### Step 2: Test URLs

**Test Python Backend:**
```bash
curl http://localhost:5000/api/health
```

**Should return:**
```json
{"cors":"enabled","message":"Chatbot API is running","status":"healthy"}
```

**Test Angular:**
Open browser: http://localhost:4200

### Step 3: Test AI Chatbot

1. **Click** purple chat button (bottom-right corner)
2. **Type**: "What is your experience?"
3. **Press** Enter

**Response should end with:** `(ML)` ← This means Python ML is connected!

### Step 4: Check Browser Console

Press `F12` → Console tab

**Should see:**
```
✅ Python ML backend is connected and ready!
```

**Should NOT see:**
```
❌ Access to XMLHttpRequest... blocked by CORS
```

---

## 🛑 How to Stop

Just press `Ctrl+C` in the terminal where you ran `./start.sh`

**You'll see:**
```
🛑 Stopping all services...
✅ All services stopped
```

Both Python and Angular will stop cleanly.

---

## 🐛 Troubleshooting

### Issue: "Permission denied: ./start.sh"

**Solution:**
```bash
chmod +x start.sh
./start.sh
```

### Issue: "Port 5000 already in use"

**Solution:**
```bash
lsof -i :5000
kill -9 <PID>
./start.sh
```

### Issue: "Port 4200 already in use"

**Solution:**
```bash
lsof -i :4200
kill -9 <PID>
./start.sh
```

### Issue: "python3: command not found"

**Solution:**
Install Python 3.8+ from python.org, then:
```bash
./start.sh
```

### Issue: "npm: command not found"

**Solution:**
Install Node.js from nodejs.org, then:
```bash
npm install
./start.sh
```

---

## 💡 Pro Tips

### Tip 1: Run in Background (Using screen)

```bash
screen -S portfolio
./start.sh

# Press Ctrl+A then D to detach
# Reattach later: screen -r portfolio
```

### Tip 2: Auto-Start on macOS

Create `~/Library/LaunchAgents/com.jahul.portfolio.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.jahul.portfolio</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/jahulkhan/Documents/workspace/personal/jahul-port-folio/start.sh</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

### Tip 3: Create Desktop Shortcut (macOS)

Create `Start Portfolio.command`:
```bash
#!/bin/bash
cd /Users/jahulkhan/Documents/workspace/personal/jahul-port-folio
./start.sh
```

Make executable:
```bash
chmod +x "Start Portfolio.command"
```

Double-click to run!

---

## 📝 Summary

**One Command:**
```bash
./start.sh
```

**Opens:**
- http://localhost:4200 (automatically in browser)

**Starts:**
- Python ML Backend (http://localhost:5000)
- Angular Frontend (http://localhost:4200)

**Stop:**
- Press Ctrl+C

**That's it!** Simplest way to run everything! 🚀✨

---

## 🎉 You're Ready!

Just run:
```bash
./start.sh
```

And your portfolio with AI chatbot will be live at:
**http://localhost:4200** 🌐

**Browser opens automatically!** 🎊
