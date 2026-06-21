from langchain_core.prompts import PromptTemplate


recommendation_prompt = PromptTemplate.from_template(
    """
    You are an expert credit card advisor.

    User Spending Summary:
    {spending}

    Available Credit Cards:
    {cards}

    Analyze the spending pattern and:

    1. Recommend the best card
    2. Explain why it fits
    3. Estimate reward potential
    4. Mention 2 alternatives
    5. Be very precise
    6. Maintain a formal tone

    Answer clearly.
    """
)