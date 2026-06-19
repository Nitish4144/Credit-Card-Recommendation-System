from pydantic import BaseModel
class RecommendationResponse( BaseModel ):
    card_name: str
    reward: float
    annual_fee: int
    net_value: float
    reason: str