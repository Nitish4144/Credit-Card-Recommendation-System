from datetime import datetime
import pandas as pd

from app.services.categorization_service import (
    categorize_transaction
)

def parse_csv(file):
    df = pd.read_csv(file)

    transactions = []

    for _, row in df.iterrows():

        transactions.append({
            "date": datetime.strptime(
                row["date"],
                "%Y-%m-%d"
            ).date(),

            "description":
                row["description"],

            "category":
                categorize_transaction(
                    row["description"]
                ),

            "amount":
                float(row["amount"])
        })

    return transactions