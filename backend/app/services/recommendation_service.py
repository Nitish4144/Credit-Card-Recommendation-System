# from app.prompts.recommendation_prompt import (build_recommendation_prompt)
from app.chroma.context_builder import build_card_context
from app.services.recommendation_chain import recommendation_chain


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
    card_names = [card["card_name"] for card in top_cards]
    card_context = build_card_context(card_names)
                    # print("DEBUG\n")
                    # print("========== CARD CONTEXT ==========")
                    # print(type(card_context))
                    # print(card_context)
                    # # print(f"card_name={name} \n and \n {card_contexti}" for name,card_contexti in zip(card_names, card_context) )
                    
                    # print("========== LLM RESPONSE ==========")
                    # print(type(response))
                    # print(response)

    for card in top_cards:
        response = recommendation_chain.invoke(
        {
            "card_context": card_context,
            "spending": spending,
            "recommendation": card  #Current Card name
        }
        )
        explanation = str(response)
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