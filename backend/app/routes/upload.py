from fastapi import APIRouter, UploadFile, File
from app.services.csv_parser import parse_csv
from sqlalchemy.orm import Session
from app.core.database import get_db
from fastapi import Depends
from app.models import Transaction

router = APIRouter()

@router.post("/upload")
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    transactions = parse_csv(file.file)

    for transaction in transactions:

        new_transaction = Transaction(
            date=transaction["date"],
            description=transaction["description"],
            category=transaction["category"],
            amount=transaction["amount"]
        )

        db.add(new_transaction)

    db.commit()

    return {
        "message": "CSV uploaded successfully",
        "count": len(transactions)
    }