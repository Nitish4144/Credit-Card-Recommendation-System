import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_explanation(prompt: str):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    result = response.json()

    return result["response"]