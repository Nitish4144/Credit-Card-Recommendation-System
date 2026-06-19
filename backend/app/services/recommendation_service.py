def calculate_reward(card, spending):

    return (
        spending["food"] * (card.food_cashback or 0) / 100 +
        spending["fuel"] * (card.fuel_cashback or 0) / 100 +
        spending["travel"] * (card.travel_cashback or 0) / 100 +
        spending["shopping"] * (card.shopping_cashback or 0) / 100 +
        spending["entertainment"] * (card.entertainment_cashback or 0) / 100 +
        spending["utilities"] * (card.utility_cashback or 0) / 100
    )


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
            "reason":
                f"Best rewards acco to my model"
        })

    recommendations.sort(
        key=lambda x: x["net_value"],
        reverse=True
    )

    return recommendations[:3]