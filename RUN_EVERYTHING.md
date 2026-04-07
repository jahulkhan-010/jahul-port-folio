# 🚀 Run Angular + Python Chatbot Together

## ✨ Three Ways to Run Both Services

I've created **3 different methods** to run both Angular and Python backend together. Choose the one that works best for you!

---

## Method 1: NPM Script (Recommended - Easiest!)

### **One Command to Rule Them All** 🎯

**macOS/Linux:**
```bash
npm run dev
```

**Windows:**
```bash
npm run dev:win
```

That's it! This will:
- ✅ Start Python backend on http://localhost:5000
- ✅ Start Angular frontend on http://localhost:4200
- ✅ Show both outputs in the same terminal with colored prefixes
- ✅ Stop both when you press Ctrl+C

**Expected Output:**
```
[PYTHON] 🤖 Starting AI Chatbot Backend...
[PYTHON] 📚 Knowledge base loaded with 10 entries
[PYTHON] 🚀 Server running on http://localhost:5000
[ANGULAR] ✔ Application bundle generation complete.
[ANGULAR] Local:   http://localhost:4200/
```

**First Time Setup:**
```bash
npm install  # Install concurrently package
cd chatbot-backend
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
cd ..
npm run dev
```

---

## Method 2: Bash Script (macOS/Linux)

### **Automated Script with Monitoring**

```bash
chmod +x start-all.sh
./start-all.sh
```

**Features:**
- ✅ Automatically creates Python virtual environment
- ✅ Installs dependencies if needed
- ✅ Starts both services in background
- ✅ Monitors both processes
- ✅ Shows status and logs
- ✅ Clean shutdown with Ctrl+C

**Expected Output:**
```
🚀 Starting Portfolio with AI Chatbot
======================================

Step 1/2: Starting Python ML Backend...
✅ Python backend started (PID: 12345)

Step 2/2: Starting Angular Frontend...
✅ Angular frontend started (PID: 12346)

======================================
🎉 All Services Running!
======================================

📊 Service Status:
  Python Backend:  http://localhost:5000 (PID: 12345)
  Angular Frontend: http://localhost:4200 (PID: 12346)

📝 Logs:
  Python:  tail -f python-backend.log
  Angular: tail -f angular-frontend.log

🌐 Open your browser:
  http://localhost:4200

⏹️  Press Ctrl+C to stop all services
```

---

## Method 3: Windows Batch File

### **For Windows Users**

Double-click `start-all.bat` or run:

```bash
start-all.bat
```

**Features:**
- ✅ Opens two separate terminal windows
- ✅ One for Python backend
- ✅ One for Angular frontend
- ✅ Easy to see logs for each service

**This will open:**
1. **Window 1:** Python ML Backend running
2. **Window 2:** Angular Frontend running

**To stop:**
- Close both windows or press Ctrl+C in each

---

## 🎯 Quick Comparison

| Method | Platform | Complexity | Best For |
|--------|----------|------------|----------|
| **npm run dev** | All | ⭐ Easy | Daily development |
| **start-all.sh** | macOS/Linux | ⭐⭐ Medium | Auto-setup & monitoring |
| **start-all.bat** | Windows | ⭐⭐ Medium | Windows users |

---

## ✅ Verification Steps

After starting with any method:

### Step 1: Check Services Running

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

### Step 2: Test AI Chatbot

1. **Open** http://localhost:4200 in browser
2. **Click** purple chat button (bottom-right)
3. **Type** "experience" and press Enter
4. **Check** response ends with `(ML)` tag

**If you see (ML)** → ✅ Python backend is connected!
**If you see (Fallback)** → ❌ Python backend not connected

### Step 3: Check Browser Console

Press `F12` → Console tab

**Should see:**
```
✅ Python ML backend is connected and ready!
```

**Should NOT see:**
```
❌ Access to XMLHttpRequest... blocked by CORS policy
```

---

## 🐛 Troubleshooting

### Issue: "concurrently: command not found"

**Solution:**
```bash
npm install
```

### Issue: Python backend fails to start

**Solution:**
```bash
cd chatbot-backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cd ..
npm run dev
```

### Issue: Port 5000 already in use

**Solution:**
```bash
# Find and kill process using port 5000
lsof -i :5000
kill -9 <PID>
```

### Issue: Port 4200 already in use

**Solution:**
```bash
# Find and kill process using port 4200
lsof -i :4200
kill -9 <PID>
```

### Issue: Still showing (Fallback) responses

**Checklist:**
- [ ] Python backend is actually running (check terminal)
- [ ] No errors in Python output
- [ ] Hard refresh browser (Ctrl+Shift+R)
- [ ] Check `curl http://localhost:5000/api/health` works
- [ ] No firewall blocking port 5000

---

## 📝 Available NPM Scripts

```bash
# Start both services together (recommended)
npm run dev          # macOS/Linux
npm run dev:win      # Windows

# Start only Angular
npm start

# Start only Python backend  
npm run backend      # macOS/Linux
npm run backend:win  # Windows

# Build for production
npm run build

# Run tests
npm test
```

---

## 🎨 Customization

### Change Python Port

Edit `chatbot-backend/app.py`, line 143:
```python
app.run(debug=True, port=5001)  # Changed from 5000
```

Also update Angular component:
- `src/app/components/chatbot/chatbot.component.ts` line 27
- Change `http://localhost:5000` to `http://localhost:5001`

### Change Angular Port

Run:
```bash
ng serve --port 4201
```

Or update `package.json`:
```json
"start": "ng serve --port 4201"
```

---

## 💡 Pro Tips

### Tip 1: Keep Terminals Organized

Using `npm run dev`:
- All output in one terminal
- Color-coded: PYTHON (blue), ANGULAR (magenta)
- Easy to see what's happening

### Tip 2: View Logs Separately

If using `start-all.sh`:
```bash
# In separate terminals
tail -f python-backend.log
tail -f angular-frontend.log
```

### Tip 3: Auto-open Browser

Add to `package.json`:
```json
"start": "ng serve --open"
```

### Tip 4: Run in Background

Using `screen` (Linux/macOS):
```bash
screen -S portfolio
./start-all.sh
# Press Ctrl+A then D to detach
# Reattach: screen -r portfolio
```

---

## 🎉 You're All Set!

**Choose your method:**

1. **Quick Start:** `npm run dev` (recommended)
2. **Auto Setup:** `./start-all.sh` (macOS/Linux)
3. **Separate Windows:** `start-all.bat` (Windows)

**Then:**
- Open http://localhost:4200
- Test the AI chatbot
- Enjoy your ML-powered portfolio!

---

## 📚 Related Files

- `package.json` - NPM scripts configuration
- `start-all.sh` - Bash script for macOS/Linux
- `start-all.bat` - Batch file for Windows
- `chatbot-backend/app.py` - Python backend
- `src/app/components/chatbot/` - Angular chatbot component

**Everything is ready! Just pick your method and run!** 🚀✨
