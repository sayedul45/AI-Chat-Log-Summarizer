# 🤖 AI Chat Log Summarizer

**AI Chat Log Summarizer** is a Python-based NLP project that reads `.txt` chat logs between a user and an AI, parses the conversation, and generates a concise summary with message statistics and frequently used keywords. It features both a **FastAPI** backend for processing and a **Streamlit** frontend for user interaction. The entire project is containerized using Docker.

---

## 📂 Project Structure
```
AIChatLogSummarizer/
├── backend/                # FastAPI backend
│   ├── main.py             # API entry point
│   ├── requirements.txt    # Backend dependencies
│   ├── chat_parser.py      # Chat parsing logic
│   ├── keyword_analyzer.py # Keyword extraction logic
│   ├── summarizer.py       # Summary generation
│   ├── utils/              # Utilities
│   │   ├── stop_words.py
│   │   └── helpers.py
│   ├── data/               # Input/output files (optional)
│   │   ├── chat_logs/
│   │   └── output/
│   └── tests/              # Unit tests
├── frontend/               # Streamlit frontend
│   ├── app.py              # Main Streamlit UI
│   ├── requirements.txt    # Frontend dependencies
│   ├── static/             # Optional static files (CSS)
│   └── components/         # Streamlit display components
├── docker-compose.yml      # Docker integration
├── sample_chat.txt         # Example input file
├── .gitignore
└── README.md               # Project documentation
```

---

## 🚀 Features
- 📤 Upload chat logs (.txt)
- 🤖 Separate User and AI messages
- 📊 Count total, user, and AI messages
- 🔑 Extract top 5 most frequent keywords
- 🧠 Generate a human-readable summary
- 💬 Streamlit web interface
- 🐳 Dockerized backend & frontend

---

## 🧰 Tech Stack
| Layer      | Tools                 |
|------------|-----------------------|
| Backend    | FastAPI, Uvicorn     |
| NLP        | NLTK, scikit-learn   |
| Frontend   | Streamlit            |
| DevOps     | Docker, Docker Compose |

---

## 🧪 Sample Chat Format
```
User: Hello!
AI: Hi! How can I assist you today?
User: Can you explain what machine learning is?
AI: Certainly! Machine learning is a field of AI that allows systems to learn from data.
```

---

## 🐳 How to Run (Dockerized Setup)

### Step 1: Prerequisites
- Install Docker: https://www.docker.com/products/docker-desktop

### Step 2: Run with Docker Compose
```bash
docker compose up --build
```

> If you are using legacy Docker: `docker-compose up --build`

### Step 3: Open the App
- 🔗 Frontend (Streamlit): http://localhost:8501
- 🔗 Backend (FastAPI Docs): http://localhost:8000/docs

---

## 💻 Manual Local Run (Without Docker)

### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend (Streamlit)
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧪 Run Tests
```bash
cd backend
pytest tests/
```

---

## 🖼️ Screenshots
> (You can paste screenshots of the Streamlit app and API docs here for demo)

---

## ✅ Summary Output Example
```
Summary:
- Total Exchanges: 6
- User Messages: 3
- AI Messages: 3
- Most Common Keywords: python, use, data, ai, learning
- Topic Hint: Conversation is mainly about python, use.
```

---

## 📁 Sample File
Use `sample_chat.txt` from the root directory to test the app.

---

## 🧠 Future Enhancements
- Download summary as .txt or .json
- Word cloud visualization
- Handle batch (multi-log) input
- Add login and save user history
- Support other languages (e.g., Bangla, Spanish)





