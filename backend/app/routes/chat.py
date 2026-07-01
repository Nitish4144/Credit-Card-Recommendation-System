from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    answer = chat(
        question=request.question,
        db=db,
        user_id=current_user.id
    )

    return chatResponse(
        answer=answer
    )