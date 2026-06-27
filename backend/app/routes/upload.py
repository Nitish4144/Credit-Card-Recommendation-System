from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import upload_service

router = APIRouter()


@router.post("/upload")
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return upload_service.upload_csv(
        file,
        db
    )


@router.delete("/transactions")
def delete_transactions(
    db: Session = Depends(get_db)
):
    return upload_service.clear_transactions(db)