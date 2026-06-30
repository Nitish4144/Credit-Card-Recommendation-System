from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)

    date = Column(Date)

    description = Column(String)

    category = Column(String)

    amount = Column(Float)

    user = relationship("User",back_populates="transactions")