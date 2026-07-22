import { useChat } from "../hooks/useChat";

import ChatInput from "./ChatInput";
import ChatWindow from "./ChatWindow";

export default function ChatBot() {

    const {
        messages,
        loading,
        error,
        send
    } = useChat();

    return (
        <div className="chat-bot" >
            <h2>AI Credit Card Assistant</h2>

            <ChatWindow
                messages={messages}
                loading={loading}
            />

            {error && (
                <p
                    style={{
                        color: "red",
                        marginBottom: "10px",
                    }}
                >
                    {error}
                </p>
            )}

            <ChatInput
                loading={loading}
                onSend={send}
            />
        </div>
    );
}