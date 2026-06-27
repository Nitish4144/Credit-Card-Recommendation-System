import type { ChatMessage as Message } from "../types/chat";

interface ChatMessageProps {
    message: Message;
}

export default function ChatMessage({
    message,
}: ChatMessageProps) {
    const isUser = message.role === "user";

    return (
        <div
            style={{
                display: "flex",
                justifyContent: isUser ? "flex-end" : "flex-start",
                marginBottom: "12px",
            }}
        >
            <div
                style={{
                    backgroundColor: isUser ? "#2563eb" : "#f3f4f6",
                    color: isUser ? "#ffffff" : "#111827",
                    padding: "10px 14px",
                    borderRadius: "12px",
                    maxWidth: "70%",
                    wordBreak: "break-word",
                }}
            >
                {message.content}
            </div>
        </div>
    );
}