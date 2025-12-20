

# 🩺 Medical Chatbot (RAG-based AI Assistant)

An **AI-powered Medical Chatbot** built using **Retrieval-Augmented Generation (RAG)** that answers medical questions based on a **preloaded medical PDF**.
The application is containerized with **Docker**, deployed on **AWS EC2**, and uses **GitHub Actions for CI/CD**.

---

## 🚀 Features

* 🔍 **RAG Architecture** (LangChain)
* 📄 Uses **preloaded medical PDF** (no user upload required)
* 🧠 **OpenAI Embeddings + GPT-4o**
* 🧾 **Pinecone Vector Database**
* ⚡ **FastAPI backend**
* 🎨 **HTML/CSS frontend**
* 🐳 **Dockerized**
* ☁️ **Deployed on AWS EC2**
* 🔄 **CI/CD with GitHub Actions**

---

## 🏗️ Tech Stack

| Layer            | Technology                      |
| ---------------- | ------------------------------- |
| Backend          | FastAPI                         |
| Frontend         | HTML, CSS                       |
| LLM              | OpenAI (GPT-4o)                 |
| Embeddings       | OpenAI `text-embedding-3-small` |
| Vector DB        | Pinecone                        |
| RAG Framework    | LangChain                       |
| Containerization | Docker                          |
| Cloud            | AWS EC2 + ECR                   |
| CI/CD            | GitHub Actions                  |

---

## 📁 Project Structure

```
medical_chatbot/
├── app.py                  # FastAPI entry point
├── src/
│   ├── service.py          # MedicalChatbotService (RAG logic)
│   ├── chat.py
│   ├── helper.py
│   └── prompt.py
├── data/
│   └── Medical_book.pdf    # Default medical knowledge source
├── web/
│   ├── index.html          # Chat UI
│   ├── style.css
│   └── bot.png
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .github/workflows/
│   └── cicd.yaml
└── README.md
```

---

## 🧠 How It Works (RAG Flow)

1. Medical PDF is **loaded & chunked**
2. Chunks are converted into **embeddings**
3. Embeddings are stored in **Pinecone**
4. User question → relevant chunks retrieved
5. GPT-4o generates answer using retrieved context

---

## ⚙️ Environment Variables

Create a `.env` file (local only):

```env
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
```

⚠️ **Do not commit `.env` to GitHub**

---

## ▶️ Run Locally (Without Docker)

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```



## 🐳 Run with Docker (Local)

```bash
docker build -t medical-chatbot .
docker run -p 8080:8080 \
  -e OPENAI_API_KEY=your_key \
  -e PINECONE_API_KEY=your_key \
  medical-chatbot
```


## ☁️ Deployment (AWS)

### Deployment Architecture

```
GitHub → GitHub Actions → AWS ECR → EC2 → Docker Container → FastAPI App
```

### CI/CD Pipeline

* **CI**: Build Docker image & push to ECR
* **CD**: Self-hosted runner on EC2 pulls image & restarts container

---



## 🔐 Security Notes

* API keys stored as **GitHub Secrets**
* EC2 runner uses **IAM Role**
* `.env` and secrets are excluded via `.gitignore` & `.dockerignore`



---

## 📌 Future Improvements

* HTTPS with Nginx + SSL
* Domain name integration
* Chat history persistence
* Authentication
* Streaming responses
* Multi-document support

---

## 👨‍💻 Author

**Yella Reddy**
AI / ML Engineer
🔗 GitHub: [https://github.com/yellareddy19](https://github.com/yellareddy19)


