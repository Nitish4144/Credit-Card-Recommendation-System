from langchain_core.prompts import PromptTemplate


recommendation_prompt = PromptTemplate.from_template(
    """
 You are a credit card expert.

    The Context for the Top 3 cards is:
    {card_context}

    User Spending:
    {spending}

    Current Card Name:
    {recommendation}

    Explain(wihtout mentioning your role):

    1. Why this cards fits
    2. Cashback estimate
    3. Benefits
    4. Tradeoffs
    6. Maintain a formal tone
    7. Give Short Answers

    Answer clearly.
    """
)