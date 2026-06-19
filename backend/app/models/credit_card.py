from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base


class CreditCard(Base):
    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    issuer = Column(String)
    network = Column(String)

    annual_fee = Column(Integer)
    joining_fee = Column(Integer)

    food_cashback = Column(Float)
    fuel_cashback = Column(Float)
    travel_cashback = Column(Float)
    shopping_cashback = Column(Float)
    entertainment_cashback = Column(Float)
    utility_cashback = Column(Float)

    reward_rate = Column(Float)

    welcome_bonus = Column(String)
    lounge_access = Column(String)
    description = Column(String)