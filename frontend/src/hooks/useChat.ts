import { useState } from "react";

import { sendMessage } from "../services/chat";

import type {
    ChatMessage
} from "../types/chat";

export function useChat() {

    const [messages, setMessages] = useState<ChatMessage[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    async function send(question: string) {

        if (!question.trim()) return;
        setLoading(true);
        setError(null);

        const userMessage: ChatMessage = {
            id: Date.now(),
            role: "user",
            content: question
        };

        setMessages(prev => [
            ...prev,
            userMessage
        ]);

        try {

            const response = await sendMessage(question);

            const aiMessage: ChatMessage = {
                id: Date.now() + 1,
                role: "assistant",
                content: response.answer
            };

            setMessages(prev => [
                ...prev,
                aiMessage
            ]);

        } catch (err) {

            setError(
                err instanceof Error
                    ? err.message
                    : "Unknown error."
            );

        } finally {

            setLoading(false);

        }
    }

    return {

        messages,

        loading,

        error,

        send

    };
}