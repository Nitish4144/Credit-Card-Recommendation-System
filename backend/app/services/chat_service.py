from sqlalchemy.orm import Session

from app.chroma.context_builder import build_card_context
from app.chroma.retriever import retrieve_cards
from app.repositories.credit_card_repository import get_all_cards
from app.services.analytics_service import get_category_spending
from app.services.recommendation_chain import chat_chain
from app.services.recommendation_service import recommend_cards


def chat(
    question: str,
    db: Session,
    user_id: int
) -> str:
    """
    Generate an AI response using personalized recommendations + RAG.
    """

    # Get user's spending profile
    spending = get_category_spending(
        db,
        user_id
    )

    # Get all credit cards
    cards = get_all_cards(db)

    # Generate top recommendations
    top_cards = recommend_cards(
        cards,
        spending
    )

    # -----------------------------
    # Recommendation Context
    # -----------------------------
    recommendation_context = (
        "Current Recommended Cards:\n\n"
    )

    card_names = []

    for i, card in enumerate(top_cards, start=1):

        recommendation_context += (
            f"{i}. {card['card_name']}\n"
            f"Expected Reward: ₹{card['reward']}\n"
            f"Annual Fee: ₹{card['annual_fee']}\n"
            f"Net Value: ₹{card['net_value']}\n\n"
        )

        card_names.append(
            card["card_name"]
        )

    # Detailed information about recommended cards
    recommended_card_context = build_card_context(
        card_names
    )

    # -----------------------------
    # RAG Retrieval
    # -----------------------------
    context_cards = 3

    docs = retrieve_cards(
        question,
        context_cards
    )

    if not docs:
        return (
            "I could not find any relevant card information "
            "to answer your question."
        )

    rag_context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # -----------------------------
    # Final Context
    # -----------------------------
    context = f"""
USER'S RECOMMENDED CARDS:

{recommendation_context}

DETAILS OF RECOMMENDED CARDS:

{recommended_card_context}

QUESTION RELEVANT CARD INFORMATION:


{rag_context}
"""

    # Generate answer
    answer = chat_chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )
    print("=" * 100)
    print(context)
    print("=" * 100)
    return answer