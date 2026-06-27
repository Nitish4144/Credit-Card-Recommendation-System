import type {
    ChatRequest,
    ChatResponse
} from "../types/chat";

const API_URL = "http://127.0.0.1:8000/chat";

export async function sendMessage(
    question: string
): Promise<ChatResponse> {

    const body: ChatRequest = {
        question
    };

    const response = await fetch(API_URL, {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(body)
    });

    if (!response.ok) {
        throw new Error("Failed to get AI response.");
    }

    return await response.json();
}