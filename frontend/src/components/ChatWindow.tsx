import ChatMessage from "./ChatMessage";
import type { ChatMessage as Message } from "../types/chat";

interface ChatWindowProps {
    messages: Message[];
}

export default function ChatWindow({
    messages,
}: ChatWindowProps) {
    return (
        <div
            style={{
                height: "400px",
                overflowY: "auto",
                border: "1px solid #d1d5db",
                borderRadius: "8px",
                padding: "16px",
                backgroundColor: "#ffffff",
                marginBottom: "16px",
            }}
        >
            {messages.length === 0 ? (
                <p
                    style={{
                        color: "#6b7280",
                        textAlign: "center",
                    }}
                >
                    Start a conversation with the AI assistant.
                </p>
            ) : (
                messages.map((message) => (
                    <ChatMessage
                        key={message.id}
                        message={message}
                    />
                ))
            )}
        </div>
    );
}