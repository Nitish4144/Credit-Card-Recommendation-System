from sqlalchemy.orm import Session

from app.repositories import transaction_repository


def get_summary(
    db: Session,
    user_id: int
):
    total_spend = transaction_repository.get_total_spend(
        db,
        user_id
    )

    transaction_count = (
        transaction_repository.get_transaction_count(
            db,
            user_id
        )
    )

    monthly = (
        transaction_repository.get_monthly_spend(
            db,
            user_id
        )
    )

    average_monthly_spend = (
        total_spend / len(monthly)
        if monthly
        else 0
    )

    return {
        "total_spend": total_spend,
        "transaction_count": transaction_count,
        "average_monthly_spend": round(
            average_monthly_spend,
            2
        )
    }


def get_dashboard_data(
    db: Session,
    user_id: int
):
    total_spend = transaction_repository.get_total_spend(
        db,
        user_id
    )

    transaction_count = (
        transaction_repository.get_transaction_count(
            db,
            user_id
        )
    )

    categories = (
        transaction_repository.get_category_breakdown(
            db,
            user_id
        )
    )

    monthly = (
        transaction_repository.get_monthly_spend(
            db,
            user_id
        )
    )

    average_monthly_spend = (
        total_spend / len(monthly)
        if monthly
        else 0
    )

    return {
        "summary": {
            "total_spend": total_spend,
            "transaction_count": transaction_count,
            "average_monthly_spend": round(
                average_monthly_spend,
                2
            )
        },
        "categories": categories,
        "monthly": monthly
    }


def get_category_spending(
    db: Session,
    user_id: int
):
    categories = (
        transaction_repository.get_category_breakdown(
            db,
            user_id
        )
    )

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