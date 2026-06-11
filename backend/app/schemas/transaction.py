from pydantic import BaseModel


class TransactionRequest(BaseModel):
    merchant: str
    amount: float
    category: str

class TransactionResponse(BaseModel):
    message: str