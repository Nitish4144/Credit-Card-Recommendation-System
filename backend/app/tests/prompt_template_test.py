from app.prompts.prompt_template import recommendation_prompt

prompt = recommendation_prompt.format(
    spending="Food: 5000, Travel: 2000",
    cards="HDFC Millennia, SBI Cashback"
)

print(prompt)



"""
 You are an expert credit card advisor.

    User Spending Summary:
    Food: 5000, Travel: 2000

    Available Credit Cards:
    HDFC Millennia, SBI Cashback

    Analyze the spending pattern and:

    1. Recommend the best card
    2. Explain why it fits
    3. Estimate reward potential
    4. Mention 2 alternatives

    Answer clearly.
"""