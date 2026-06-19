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


def get_transaction_count(
    db: Session
) -> int:
    return db.query(Transaction).count()


def get_summary(db: Session):
    total_spend = get_total_spend(db)

    transaction_count = (
        get_transaction_count(db)
    )

    monthly = get_monthly_spend(db)

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

def get_category_breakdown(db: Session):
    rows = (
        db.query(
            Transaction.category,
            func.sum(Transaction.amount)
        ).group_by(Transaction.category).all()
    ) 

                                    # the above is equivalent to the following SQL cmd
                                    #     SELECT
                                    #         category
                                    #         SUM(amount)
                                    #     FROM transactions
                                    #     GROUP BY category;  

    return [                            # returns catgry,amnt
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


                                                        # SELECT
                                                        #     DATE_TRUNC('month', date) AS month,
                                                        #     SUM(amount) AS total_amount
                                                        # FROM transactions
                                                        # GROUP BY
                                                        #     DATE_TRUNC('month', date)
                                                        # ORDER BY
                                                        #     DATE_TRUNC('month', date);

    return [
        {
            "month": month.strftime(
                "%b %Y"
            ),
            "amount": float(amount)
        }
        for month, amount in rows
    ]



def get_dashboard_data(
    db: Session
):
    total_spend = get_total_spend(db)

    transaction_count = (
        get_transaction_count(db)
    )

    categories = (
        get_category_breakdown(db)
    )

    monthly = (
        get_monthly_spend(db)
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

    categories = get_category_breakdown(db)

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