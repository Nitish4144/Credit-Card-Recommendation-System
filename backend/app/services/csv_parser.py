import pandas as pd


def parse_csv(file):
    df = pd.read_csv(file)

    transactions = []

    for ind, row in df.iterrows():
        transactions.append(
            {
                "date": row["date"],
                "description": row["description"],
                "category": row["category"],
                "amount": float(row["amount"]),
            }
        )

    return transactions