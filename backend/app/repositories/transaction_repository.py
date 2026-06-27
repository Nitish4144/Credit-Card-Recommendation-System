from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.transaction import Transaction


def get_total_spend(db: Session) -> float:
    total = (
        db.query(
            func.coalesce(
                func.sum(Transaction.amount),
                0
            )
        )
        .scalar()
    )

    return float(total)


def get_transaction_count(db: Session) -> int:
    return db.query(Transaction).count()


def get_category_breakdown(db: Session):
    rows = (
        db.query(
            Transaction.category,
            func.sum(Transaction.amount)
        )
        .group_by(Transaction.category)
        .all()
    )

    return [
        {
            "category": category,
            "amount": float(amount)
        }
        for category, amount in rows
    ]


def get_monthly_spend(db: Session):
    rows = (
        db.query(
            func.date_trunc(
                "month",
                Transaction.date
            ),
            func.sum(Transaction.amount)
        )
        .group_by(
            func.date_trunc(
                "month",
                Transaction.date
            )
        )
        .order_by(
            func.date_trunc(
                "month",
                Transaction.date
            )
        )
        .all()
    )

    return [
        {
            "month": month.strftime("%b %Y"),
            "amount": float(amount)
        }
        for month, amount in rows
    ]


def save_transactions(
    db: Session,
    transactions: list
):
    for transaction in transactions:

        db.add(
            Transaction(
                date=transaction["date"],
                description=transaction["description"],
                category=transaction["category"],
                amount=transaction["amount"]
            )
        )

    db.commit()


def delete_all_transactions(db: Session):
    db.query(Transaction).delete()
    db.commit()