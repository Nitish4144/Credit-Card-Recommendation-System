from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import upload_service
from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/upload")
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return upload_service.upload_csv(
        file=file,
        db=db,
        user_id=current_user.id
    )


@router.delete("/transactions")
def delete_transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return upload_service.clear_transactions(
        db=db,
        user_id=current_user.id
    )