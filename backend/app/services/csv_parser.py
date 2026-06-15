import pandas as pd

from app.services.categorization_service import categorize_transaction

def parse_csv(file):
    df = pd.read_csv(file)

    transactions = []

    for ind, row in df.iterrows():

        category = categorize_transaction(row["description"])
        
        transactions.append(
            {
                "date": row["date"],
                "description": row["description"],
                "category": category,
                "amount": float(row["amount"]),
            }
        )

    return transactions