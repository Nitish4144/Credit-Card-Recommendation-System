import pandas as pd
import psycopg2
import os

conn = psycopg2.connect(
    host="localhost",
    database="creditcarddb",
    user="postgres",
    password="Nitish@4144"
)

df = pd.read_csv("../database/creditcarddb.csv")

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO credit_cards(
            name,
            issuer,
            network,
            annual_fee,
            joining_fee,
            food_cashback,
            fuel_cashback,
            travel_cashback,
            shopping_cashback,
            entertainment_cashback,
            utility_cashback,
            reward_rate,
            welcome_bonus,
            lounge_access,
            description
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        tuple(row)
    )

conn.commit()
cursor.close()
conn.close()

print("Cards inserted successfully")