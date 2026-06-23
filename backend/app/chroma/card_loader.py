import os
# print("Current working dir:", os.getcwd())

from langchain_core.documents import Document
import json
def load_card_documents():
    
    path = "../data/card_documents.json"
    if not os.path.exists(path):
        path = "app/data/card_documents.json"

        
    with open(path, "r", encoding="utf-8") as f:
        cards = json.load(f)

    documents = []

    for card in cards:
        content = card["content"]

        text = f"""
Card Name: {card['name']}
Issuer: {content['issuer']}
Network: {content['network']}

Annual Fee: ₹{content['annual_fee']}
Joining Fee: ₹{content['joining_fee']}

Food Cashback: {content['food_cashback']}%
Fuel Cashback: {content['fuel_cashback']}%
Travel Cashback: {content['travel_cashback']}%
Shopping Cashback: {content['shopping_cashback']}%
Entertainment Cashback: {content['entertainment_cashback']}%
Utility Cashback: {content['utility_cashback']}%

Base Reward Rate: {content['reward_rate']}%

Welcome Bonus: ₹{content['welcome_bonus']}

Lounge Access Visits: {content['lounge_access']}

Description:
{content['description']}
"""

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "card_name": card["name"],
                    "issuer": content["issuer"],
                    "network": content["network"]
                }
            )
        )

    return documents