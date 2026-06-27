from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import logger
from app.models import Transaction
from app.services.csv_parser import parse_csv

router = APIRouter()


@router.post("/upload")
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    logger.info(f"Received CSV upload: {file.filename}")

    transactions = parse_csv(file.file)

    logger.info(f"Parsed {len(transactions)} transactions")

    for transaction in transactions:

        new_transaction = Transaction(
            date=transaction["date"],
            description=transaction["description"],
            category=transaction["category"],
            amount=transaction["amount"]
        )

        db.add(new_transaction)

    db.commit()

    logger.info(
        f"Successfully inserted {len(transactions)} transactions"
    )

    return {
        "message": "CSV uploaded successfully",
        "count": len(transactions)
    }