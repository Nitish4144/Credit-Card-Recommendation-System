from langchain_core.prompts import PromptTemplate


recommendation_prompt = PromptTemplate.from_template(
 """
You are an expert financial advisor.

Use only the information provided below.

Card Information:
{card_context}

User Spending:
{spending}

Current Recommended Card:
{recommendation}

Write a single,short(and concise) well-structured paragraph (80-120 words) explaining why this credit card is a good recommendation for the user.

Your explanation should:
- Explain why the card matches the user's spending habits.
- Naturally mention the estimated annual reward, annual fee, and net value.
- Highlight the most valuable benefits of the card.
- Mention one important limitation or tradeoff if applicable.
- Maintain a professional, helpful, and concise tone.
- Do not use bullet points, numbering, headings, markdown, or question-answer format.
- Do not mention that you are an AI or financial advisor.
- Do not invent information that is not present in the provided context.

Return only the paragraph.
"""
)