from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.transaction import Transaction


def get_total_spend(
    db: Session,
    user_id: int
) -> float:
    total = (
        db.query(
            func.coalesce(
                func.sum(Transaction.amount),
                0
            )
        )
        .filter(Transaction.user_id == user_id)
        .scalar()
    )

    return float(total)


def get_transaction_count(
    db: Session,
    user_id: int
) -> int:
    return (
        db.query(Transaction)
        .filter(Transaction.user_id == user_id)
        .count()
    )


def get_category_breakdown(
    db: Session,
    user_id: int
):
    rows = (
        db.query(
            Transaction.category,
            func.sum(Transaction.amount)
        )
        .filter(Transaction.user_id == user_id)
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


def get_monthly_spend(
    db: Session,
    user_id: int
):
    rows = (
        db.query(
            func.date_trunc(
                "month",
                Transaction.date
            ),
            func.sum(Transaction.amount)
        )
        .filter(Transaction.user_id == user_id)
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
    transactions: list,
    user_id: int
):
    for transaction in transactions:
        db.add(
            Transaction(
                user_id=user_id,
                date=transaction["date"],
                description=transaction["description"],
                category=transaction["category"],
                amount=transaction["amount"]
            )
        )

    db.commit()


def delete_user_transactions(
    db: Session,
    user_id: int
):
    (
        db.query(Transaction)
        .filter(Transaction.user_id == user_id)
        .delete()
    )

    db.commit()