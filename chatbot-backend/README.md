# AI Chatbot Backend for Portfolio

This is an AI-powered chatbot backend built with Flask and Sentence Transformers that answers questions about Jahul Khan's professional experience, skills, and projects.

## Features

- **Semantic Search**: Uses `sentence-transformers` for understanding user questions
- **Knowledge Base**: Pre-loaded with information about work experience, skills, projects, and achievements
- **RESTful API**: Simple API endpoints for chat functionality
- **CORS Enabled**: Ready to connect with Angular frontend

## Setup Instructions

### 1. Create Virtual Environment

```bash
cd chatbot-backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Flask-CORS (for cross-origin requests)
- sentence-transformers (for semantic similarity)
- scikit-learn (for cosine similarity)
- numpy (for numerical operations)
- torch (PyTorch for ML models)

### 3. Run the Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

### 4. Test the API

**Health Check:**
```bash
curl http://localhost:5000/api/health
```

**Chat Request:**
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Jahul'\''s experience?"}'
```

## API Endpoints

### POST /api/chat
Send a question and receive an AI-generated answer.

**Request:**
```json
{
  "question": "What projects has Jahul worked on?"
}
```

**Response:**
```json
{
  "response": "Jahul's main project is the Visa2Fly ecosystem...",
  "status": "success"
}
```

### GET /api/health
Check if the API is running.

**Response:**
```json
{
  "status": "healthy",
  "message": "Chatbot API is running"
}
```

## How It Works

1. **Sentence Transformers**: Uses `all-MiniLM-L6-v2` model to convert questions and answers into vector embeddings
2. **Cosine Similarity**: Calculates similarity between user question and knowledge base
3. **Best Match**: Returns the most relevant answer based on similarity score
4. **Fallback**: If no good match is found, returns a helpful general response

## Knowledge Base Categories

- Work Experience
- Current Role
- Technical Skills
- Visa2Fly Project
- White-Label Integrations
- Achievements
- Contact Information
- Frontend Expertise
- Education Background
- Projects Portfolio

## Customization

To add more knowledge, edit the `KNOWLEDGE_BASE` array in `app.py`:

```python
{
    "category": "new_topic",
    "question": "Sample question about the topic",
    "answer": "Detailed answer with relevant information"
}
```

## Production Deployment

For production, consider:
- Using gunicorn or uwsgi instead of Flask development server
- Adding authentication/rate limiting
- Deploying to cloud platforms (AWS, Heroku, Google Cloud)
- Using environment variables for configuration

## Notes

- First run will download the ML model (~80MB)
- Model inference is fast (~50ms per query)
- Supports unlimited concurrent requests
- Similarity threshold is set to 0.3 (adjustable in code)
