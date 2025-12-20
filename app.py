from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.service import MedicalChatbotService

app = FastAPI()

app.mount("/web", StaticFiles(directory="web"), name="web")

svc = MedicalChatbotService()

@app.on_event("startup")
def startup():
    svc.setup()

@app.get("/", response_class=HTMLResponse)
def home():
    with open("web/index.html", "r", encoding="utf-8") as f:
        return f.read()

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


@app.post("/chat")
def chat(req: ChatRequest):
    answer = svc.ask(req.message, session_id=req.session_id)
    return {"answer": answer}

