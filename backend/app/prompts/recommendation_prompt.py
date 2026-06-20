def build_recommendation_prompt(
    card_name,
    annual_fee,
    reward,
    food,
    fuel,
    travel,
    shopping,
    entertainment,
):
    return f"""
You are a credit card advisor.

Card Name:
{card_name}

Annual Fee:
₹{annual_fee}

Projected Reward:
₹{reward}

User Spending:

Food:
₹{food}

Fuel:
₹{fuel}

Travel:
₹{travel}

Shopping:
₹{shopping}

Entertainment:
₹{entertainment}

Explain in 3-5 sentences why this card is suitable.

Mention the spending categories that influenced the recommendation.

Keep the response concise and professional.
"""