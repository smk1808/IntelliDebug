from fastapi import APIRouter
from services.codebase_chat import chat_with_codebase

router = APIRouter(tags=["Codebase Chat"])

@router.post("/chat-codebase")

def chat(data: dict):

    question = data["question"]
    codebase = data["codebase"]
    answer = chat_with_codebase(question, codebase)
    return {"answer": answer}
