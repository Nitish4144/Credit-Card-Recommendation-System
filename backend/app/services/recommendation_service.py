from app.prompts.recommendation_prompt import (build_recommendation_prompt)

from app.services.ollama_service import (generate_explanation)


def calculate_reward(card, spending):
    return (
        spending.get("food", 0) * (card.food_cashback or 0) / 100 +
        spending.get("fuel", 0) * (card.fuel_cashback or 0) / 100 +
        spending.get("travel", 0) * (card.travel_cashback or 0) / 100 +
        spending.get("shopping", 0) * (card.shopping_cashback or 0) / 100 +
        spending.get("entertainment", 0) * (card.entertainment_cashback or 0) / 100 +
        spending.get("utilities", 0) * (card.utility_cashback or 0) / 100
    )


def attach_explanations(top_cards, spending):

    for card in top_cards:

        prompt = build_recommendation_prompt(
            card_name=card["card_name"],
            annual_fee=card["annual_fee"],
            reward=card["reward"],
            food=spending.get("food", 0),
            fuel=spending.get("fuel", 0),
            travel=spending.get("travel", 0),
            shopping=spending.get("shopping", 0),
            entertainment=spending.get("entertainment", 0)
        )

        try:
            explanation = generate_explanation(prompt)
        except Exception:
            explanation = "AI explanation unavailable."
        card["explanation"] = explanation

    return top_cards

# def attach_explanations(top_cards, spending):

#     for card in top_cards:
#         card["explanation"] = "Test explanation"

#     return top_cards

def recommend_cards(cards, spending):

    recommendations = []

    for card in cards:

        annual_reward = calculate_reward(card, spending) * 12

        net_value = annual_reward - (card.annual_fee or 0)

        recommendations.append({
            "card_name": card.name,
            "reward": round(annual_reward, 2),
            "annual_fee": card.annual_fee,
            "net_value": round(net_value, 2),
        })

    recommendations.sort(
        key=lambda x: x["net_value"],
        reverse=True
    )

    top_cards = recommendations[:3]

    top_cards = attach_explanations(
        top_cards,
        spending
    )

    return top_cards