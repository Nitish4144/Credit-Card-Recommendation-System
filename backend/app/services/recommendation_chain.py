from app.services.prompt_template import recommendation_prompt
from app.services.llm_service import llm

recommendation_chain = recommendation_prompt | llm


# response = recommendation_chain.invoke(
#     {
#         "spending": "Food: ₹10000",
#         "cards": "SBI Cashback Card"
#     }
# )

# print(response)