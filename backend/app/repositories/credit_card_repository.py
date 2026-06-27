from sqlalchemy.orm import Session

from app.models.credit_card import CreditCard


def get_all_cards(db: Session):
    return db.query(CreditCard).all()


def get_card_count(db: Session):
    return db.query(CreditCard).count()