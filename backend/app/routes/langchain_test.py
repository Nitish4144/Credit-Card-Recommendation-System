from fastapi import APIRouter

from app.services.recommendation_chain import recommendation_chain


router = APIRouter(
    prefix="/langchain",
    tags = ["LangChain"]
)

@router.get("/test")
def test():

    result = recommendation_chain.invoke(
        {
             "spending": "Food ₹10000, Travel ₹5000",
            "cards": """
            SBI Cashback Card
            HDFC Millennia
            Axis Ace
            """
        } #promt
    )

    return {
        "response": result
    }