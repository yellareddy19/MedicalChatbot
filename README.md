
# 🩺 Medical Chatbot (RAG-based)

A Retrieval-Augmented Generation (RAG) based **Medical Chatbot** built using **LangChain, OpenAI, Pinecone**, and a **modern HTML/CSS frontend**.  
The chatbot answers medical questions using a **default medical PDF** stored locally (no document upload by users).

---

## ✨ Features

- 📄 Uses a **preloaded medical PDF** (`data/Medical_book.pdf`)
- 🔍 Semantic search using **OpenAI embeddings**
- 🧠 Context-aware answers using **GPT-4o**
- 🧬 Vector storage with **Pinecone**
- ⚡ Modular, production-ready Python code
- 🎨 Beautiful chatbot UI built with **HTML, CSS, JavaScript**
- 🚫 No document upload needed by users

---

## 🧱 Tech Stack

### Backend
- Python
- LangChain
- OpenAI (`text-embedding-3-small`, `gpt-4o`)
- Pinecone (Vector Database)
- FastAPI

### Frontend
- HTML
- CSS
- JavaScript

---

## 📁 Project Structure

```text
MED_CHATBOT/
├─ data/
│  └─ Medical_book.pdf
├─ src/
│  ├─ ingest.py
│  ├─ embeddings.py
│  ├─ pinecone_db.py
│  ├─ rag.py
│  ├─ service.py
│  └─ __init__.py
├─ web/
│  ├─ index.html
│  ├─ style.css
│  ├─ app.js
│  └─ assets/
│     └─ bot.png
├─ app.py
├─ requirements.txt
├─ setup.py
├─ .env
├─ .gitignore
└─ README.md
````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/MedicalChatbot.git
cd MedicalChatbot
```

---

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows (Git Bash)
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or editable install:

```bash
pip install -e .
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

⚠️ **Do NOT commit `.env`**

---

## 🚀 Run the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 💬 How It Works

```text
Medical PDF
   ↓
Text Chunking
   ↓
OpenAI Embeddings
   ↓
Pinecone Vector Database
   ↓
Retriever
   ↓
GPT-4o Response
```

---

## 🧪 Example Query

**User:**

> What is anemia?

**Bot:**
Retrieves relevant content from the medical book and generates a grounded medical explanation.

---

## 🔐 Security Notes

* `.env` is ignored via `.gitignore`
* API keys are never pushed to GitHub
* Rotate keys immediately if exposed

---





