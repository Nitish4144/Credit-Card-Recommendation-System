from fastapi import APIRouter, Depends

from app.schemas.chat import ChatRequest, chatResponse
from app.services.chat_service import chat

from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "",
    response_model=chatResponse
)
def chat_endpoint(
    request: ChatRequest,
    current_user: User = Depends(get_current_user)
):
    answer = chat(
        request.question
    )

    return chatResponse(
        answer=answer
    )