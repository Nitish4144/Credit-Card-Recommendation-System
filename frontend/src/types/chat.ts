export interface ChatRequest {
    question: string;
}

export interface ChatResponse {
    answer: string;
}

export interface ChatMessage {
    id: number;
    role: "user" | "assistant";
    content: string;
}