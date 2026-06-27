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
        <div
            style={{
                marginTop: "20px",
                padding: "20px",
                border: "1px solid #ddd",
                borderRadius: "10px",
                backgroundColor: "#fafafa",
            }}
        >
            <h2>AI Credit Card Assistant</h2>

            <ChatWindow
                messages={messages}
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