import ChatMessage from "./ChatMessage";
import type { ChatMessage as Message } from "../types/chat";

interface ChatWindowProps {
    messages: Message[];
}

export default function ChatWindow({
    messages,
}: ChatWindowProps) {
    return (
        <div className="chat-window" >
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