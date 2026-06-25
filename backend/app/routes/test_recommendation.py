from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.credit_card import CreditCard
from app.services.recommendation_service import recommend_cards

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.get("/")
def get_recommendations(db: Session = Depends(get_db)):

    cards = db.query(CreditCard).all()

    spending = {
        "food": 5000,
        "fuel": 2000,
        "travel": 8000,
        "shopping": 10000,
        "utilities": 3000,
        "entertainment": 2000
    }

    return recommend_cards(cards, spending)