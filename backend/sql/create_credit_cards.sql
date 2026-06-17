CREATE TABLE IF NOT EXISTS credit_cards(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    issuer VARCHAR(100),
    network VARCHAR(50),

    annual_fee INTEGER,
    joining_fee INTEGER,

    food_cashback FLOAT,
    fuel_cashback FLOAT,
    travel_cashback FLOAT,
    shopping_cashback FLOAT,
    entertainment_cashback FLOAT,
    utility_cashback FLOAT,

    reward_rate FLOAT,

    welcome_bonus TEXT,

    lounge_access BOOLEAN DEFAULT FALSE,

    description TEXT
);