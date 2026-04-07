# 🗄️ MongoDB Setup Guide - Local & Production

## ✅ Complete MongoDB Integration for AI Chatbot

Your chatbot now uses MongoDB for storing conversations in both development and production!

---

## 📋 **Quick Summary:**

| Environment | Database | Storage |
|-------------|----------|---------|
| **Development** | MongoDB Local | localhost:27017 |
| **Production** | MongoDB Atlas | Cloud Database (Free) |

---

## 🚀 **Step 1: Install MongoDB Locally (macOS)**

### **Install MongoDB:**

```bash
# Install MongoDB via Homebrew
brew tap mongodb/brew
brew install mongodb-community@7.0

# Start MongoDB service
brew services start mongodb-community@7.0

# Verify installation
mongosh

# You should see MongoDB shell
# Type: exit
```

###  **If MongoDB doesn't start:**

```bash
# Create data directory
sudo mkdir -p /usr/local/var/mongodb
sudo chown -R $(whoami) /usr/local/var/mongodb

# Create log directory
sudo mkdir -p /usr/local/var/log/mongodb
sudo chown -R $(whoami) /usr/local/var/log/mongodb

# Start MongoDB
brew services restart mongodb-community@7.0
```

---

## 🌐 **Step 2: Create MongoDB Atlas (Production)**

### **Create Free Cloud Database:**

1. **Sign up:**
   ```
   https://www.mongodb.com/cloud/atlas/register
   ```

2. **Create Cluster:**
   - Click "Build a Database"
   - Choose **"M0 Free"** tier (512MB FREE forever!)
   - Region: Choose closest to you
   - Cluster Name: `jahul-chatbot`
   - Click "Create"

3. **Create Database User:**
   - Username: `jahul-admin`
   - Password: **Click "Autogenerate Secure Password"**
   - **COPY AND SAVE THIS PASSWORD!**
   - Click "Create User"

4. **Network Access:**
   - Click "Network Access" (left menu)
   - Click "Add IP Address"
   - Click "Allow Access from Anywhere"
   - IP Address: `0.0.0.0/0` (for Cloud Functions)
   - Click "Confirm"

5. **Get Connection String:**
   - Click "Database" → "Connect"
   - Choose "Drivers"
   - Copy connection string:
   ```
   mongodb+srv://jahul-admin:<password>@jahul-chatbot.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
   - **Save this string!**

---

## 🔧 **Step 3: Configure Local Development:**

### **Update `.env` file:**

```bash
cd chatbot-backend
nano .env
```

**Replace with your actual MongoDB Atlas password:**

```env
# MongoDB Configuration

# Local Development
MONGODB_LOCAL_URI=mongodb://localhost:27017/
MONGODB_LOCAL_DB=jahul_chatbot

# Production (MongoDB Atlas)
# Replace <password> with your ACTUAL password
MONGODB_ATLAS_URI=mongodb+srv://jahul-admin:YOUR_ACTUAL_PASSWORD@jahul-chatbot.xxxxx.mongodb.net/?retryWrites=true&w=majority
MONGODB_ATLAS_DB=jahul_chatbot_prod

# Environment
ENVIRONMENT=development
```

**Save and exit** (Ctrl+X, then Y, then Enter)

### **Install Python Dependencies:**

```bash
cd chatbot-backend
source venv/bin/activate
pip install pymongo python-dotenv
```

---

## 🚀 **Step 4: Run with MongoDB:**

### **Start MongoDB-Integrated Backend:**

```bash
cd chatbot-backend
source venv/bin/activate
python app_mongodb.py
```

**Expected Output:**
```
================================================================================
🧠 AI Chatbot with MongoDB Integration
================================================================================
📚 Base Knowledge: 16 categories
💾 MongoDB: ✅ Connected
🌐 Environment: development

🚀 Server: http://localhost:5001
🌐 CORS: Enabled
⚡ Learning: MongoDB-based
================================================================================

💻 Connecting to Local MongoDB (Development)...
✅ Connected to MongoDB: jahul_chatbot
📊 Environment: development
✅ Database indexes created
```

---

## 🧪 **Step 5: Test MongoDB Integration:**

### **Test 1: Health Check**

```bash
curl http://localhost:5001/api/health
```

**Should return:**
```json
{
  "status": "healthy",
  "message": "AI Chatbot with MongoDB",
  "mongodb_connected": true,
  "environment": "development",
  "stats": {
    "total_conversations": 0,
    "connected": true
  }
}
```

### **Test 2: Send a Question**

```bash
curl -X POST http://localhost:5001/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What is your experience?"}'
```

### **Test 3: Check MongoDB**

```bash
# Open MongoDB shell
mongosh

# Switch to database
use jahul_chatbot

# View conversations
db.conversations.find().pretty()

# You should see your question saved!
# Type: exit
```

### **Test 4: Get Statistics**

```bash
curl http://localhost:5001/api/stats
```

---

## 🌐 **Step 6: Configure Production (Cloud Functions):**

### **Update Cloud Functions Environment:**

```bash
cd functions
nano .env.yaml
```

**Replace with YOUR actual MongoDB Atlas credentials:**

```yaml
MONGODB_ATLAS_URI: "mongodb+srv://jahul-admin:YOUR_ACTUAL_PASSWORD@jahul-chatbot.xxxxx.mongodb.net/?retryWrites=true&w=majority"
MONGODB_ATLAS_DB: "jahul_chatbot_prod"
ENVIRONMENT: "production"
```

**Save and exit**

### **Deploy to Firebase:**

First, make sure you have Blaze plan enabled (required for Cloud Functions):

```bash
# Deploy functions with environment variables
firebase deploy --only functions
```

**If deployment successful, test production:**

```bash
curl https://us-central1-jahul-portfolio.cloudfunctions.net/chatbot/health
```

---

## 📊 **MongoDB Collections:**

### **conversations**
```javascript
{
  _id: ObjectId("..."),
  question: "What is your experience?",
  answer: "Jahul has 4+ years...",
  source: "ai_response",
  timestamp: ISODate("2024-01-15T10:30:00Z"),
  question_lower: "what is your experience?",
  environment: "development"
}
```

---

## ✅ **Verification Checklist:**

### **Local Development:**
- [ ] MongoDB installed and running
- [ ] `.env` file configured
- [ ] Dependencies installed (`pymongo`, `python-dotenv`)
- [ ] `python app_mongodb.py` starts successfully
- [ ] MongoDB connection successful
- [ ] Health check returns `mongodb_connected: true`
- [ ] Conversations saved to local MongoDB

### **Production:**
- [ ] MongoDB Atlas cluster created
- [ ] Database user created
- [ ] Network access configured (0.0.0.0/0)
- [ ] Connection string saved
- [ ] `functions/.env.yaml` configured
- [ ] Firebase Functions deployed
- [ ] Production health check works
- [ ] Conversations saved to Atlas

---

## 🎯 **What's Next:**

1. **Run MongoDB version locally:**
   ```bash
   python app_mongodb.py
   ```

2. **Test in browser:**
   - Open http://localhost:4200
   - Ask questions
   - Verify saved to MongoDB

3. **Deploy to production:**
   ```bash
   # After configuring .env.yaml
   firebase deploy --only functions
   ```

---

## 💡 **Tips:**

- **Local:** Uses MongoDB on `localhost:27017`
- **Production:** Uses MongoDB Atlas (cloud)
- **Automatic fallback:** If MongoDB fails, uses JSON file
- **Free tier:** MongoDB Atlas M0 is FREE forever (512MB)
- **Indexed:** Optimized for fast search
- **Learning:** AI learns from every conversation

---

**Your chatbot now has persistent MongoDB storage in dev AND production!** 🗄️✅🎉
