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
            className={isUser ? "message-row user" : "message-row ai"}
        >
            <div
                className={isUser ? "message user-message" : "message ai-message"}
            >
                {message.content}
            </div>
        </div>
    );
}