from app.services.ollama_service import generate_explanation

print(
    generate_explanation(
        "Why is SBI Cashback good?"
    )
)