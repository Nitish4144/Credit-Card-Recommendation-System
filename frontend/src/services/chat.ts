import api from "./api";

import type {
    ChatRequest,
    ChatResponse,
} from "../types/chat";

export async function sendMessage(
    question: string
): Promise<ChatResponse> {

    const body: ChatRequest = {
        question,
    };

    const response = await api.post(
        "/chat",
        body
    );

    return response.data;
}