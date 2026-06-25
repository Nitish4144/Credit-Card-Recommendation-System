from app.chroma.retriever import retrieve_cards
# print(retrieve_cards._collection.count())
from app.chroma.retriever import vector_db

print(vector_db._collection.count())
from app.prompts.chat_prompt import chat_prompt
from app.services.llm_service import llm
from app.services.recommendation_chain import chat_chain
def chat( question:str) -> str:
    """
    Generate an AI response using RAg
    """
    
    context_cards = 3
    docs = retrieve_cards(question,context_cards)

    if not docs: 
        return (
        "I could not find any relevant card information \n to answer your question"
    )

    context = "\n\n".join(doc.page_content for doc in docs)

    answer = chat_chain.invoke({
        "context": context,
        "question": question,
    })
    # print(answer)
    return answer