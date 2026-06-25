from fastapi import APIRouter

from app.schemas.chat import ChatRequest, chatResponse
from app.services.chat_service import chat

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post(
    "",
    response_model=chatResponse
)
def chat_endpoint(request: ChatRequest):
    answer = chat(request.question)

    return chatResponse(answer=answer)