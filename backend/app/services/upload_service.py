from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.logger import logger
from app.repositories import transaction_repository
from app.services.csv_parser import parse_csv


def upload_csv(
    file: UploadFile,
    db: Session
):
    logger.info(
        "Received CSV upload: %s",
        file.filename
    )

    transactions = parse_csv(file.file)

    logger.info(
        "Parsed %d transactions",
        len(transactions)
    )

    transaction_repository.save_transactions(
        db,
        transactions
    )

    logger.info(
        "Inserted %d transactions",
        len(transactions)
    )

    return {
        "message": "CSV uploaded successfully",
        "count": len(transactions)
    }

def clear_transactions(db: Session):
    transaction_repository.delete_all_transactions(db)

    return {
        "message": "All transactions deleted successfully."
    }