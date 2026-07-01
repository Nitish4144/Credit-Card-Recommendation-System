from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories import credit_card_repository
from app.services.recommendation_service import recommend_cards
from app.services.analytics_service import get_category_spending

from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)

car =None
spar =None

@router.get("/")
def get_recommendations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    cards = credit_card_repository.get_all_cards(db)

    spending = get_category_spending(
        db,
        current_user.id
    )
    car = cards
    spar = spending

    return recommend_cards(
        cards,
        spending
    )


@router.get("/test")
def test_cards(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return {
        "count": credit_card_repository.get_card_count(db)
    }