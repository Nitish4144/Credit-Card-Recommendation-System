from app.prompts.prompt_template import recommendation_prompt
from app.prompts.chat_prompt import chat_prompt
from app.services.llm_service import llm

recommendation_chain = recommendation_prompt | llm
chat_chain = chat_prompt | llm
