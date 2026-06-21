from sqlalchemy.orm import Session
from app.models.credit_card import CreditCard


def load_cards(db: Session):
    return db.query(CreditCard).all()
