from app.services.prompt_template import recommendation_prompt
from app.services.llm_service import llm

recommendation_chain = recommendation_prompt | llm

