CATEGORY_KEYWORDS = {
    "Food": [
        "starbucks",
        "swiggy",
        "zomato",
        "restaurant",
        "cafe",
        "pizza",
        "dominos",
        "kfc",
        "mcdonald"
    ],

    "Fuel": [
        "petrol",
        "fuel",
        "indian oil",
        "bharat petroleum",
        "hp petrol"
    ],

    "Travel": [
        "uber",
        "ola",
        "rapido",
        "irctc",
        "metro",
        "air india"
    ],

    "Utilities": [
        "electricity",
        "water bill",
        "wifi",
        "internet",
        "broadband",
        "mobile recharge"
    ],

    "Shopping": [
        "amazon",
        "flipkart",
        "myntra",
        "ajio"
    ],

    "Entertainment": [
        "netflix",
        "spotify",
        "youtube",
        "hotstar",
        "prime video"
    ]
}


def categorize_transaction(description: str) -> str:
    description = description.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():   #keys,values
        for keyword in keywords:
            if keyword in description:
                return category

    return "Other"