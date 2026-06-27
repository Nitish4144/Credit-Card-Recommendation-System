from sqlalchemy.orm import Session

from app.repositories import transaction_repository
from app.models.transaction import Transaction
from app.repositories import transaction_repository

def get_summary(db: Session):
    total_spend = transaction_repository.get_total_spend(db)

    transaction_count = (
        transaction_repository.get_transaction_count(db)
    )

    monthly = transaction_repository.get_monthly_spend(db)

    average_monthly_spend = (
        total_spend / len(monthly)
        if monthly
        else 0
    )

    return {
        "total_spend": total_spend,
        "transaction_count":
            transaction_count,
        "average_monthly_spend":
            round(
                average_monthly_spend,
                2
            )
    }


def get_dashboard_data(
    db: Session
):
    total_spend = transaction_repository.get_total_spend(db)

    transaction_count = (
        transaction_repository.get_transaction_count(db)
    )

    categories = (
        transaction_repository.get_category_breakdown(db)
    )

    monthly = (
        transaction_repository.get_monthly_spend(db)
    )

    average_monthly_spend = (
        total_spend / len(monthly)
        if monthly
        else 0
    )

    return {
        "summary": {
            "total_spend": total_spend,
            "transaction_count":
                transaction_count,
            "average_monthly_spend":
                round(
                    average_monthly_spend,
                    2
                )
        },
        "categories": categories,
        "monthly": monthly
    }



def get_category_spending(db: Session):

    categories = transaction_repository.get_category_breakdown(db)

    spending = {
        "food": 0,
        "fuel": 0,
        "travel": 0,
        "shopping": 0,
        "entertainment": 0,
        "utilities": 0
    }

    for item in categories:

        category = item["category"].lower()

        if category in spending:
            spending[category] = item["amount"]

    return spending