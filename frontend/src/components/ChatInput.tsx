import { useState } from "react";

interface Props {

    onSend(
        question: string
    ): void;

    loading: boolean;

}

export default function ChatInput({
    onSend,
    loading
}: Props) {

    const [question, setQuestion] = useState("");

    function handleSubmit() {

        if (!question.trim()) return;

        onSend(question);

        setQuestion("");

    }

    return (

        <div className="chat-input-container">
            <input
                className="chat-input"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Ask about credit cards..."
            />

            <button
                className="chat-send-button"
                onClick={handleSubmit}
                disabled={loading}
            >
                {loading ? "Thinking..." : "Send"}
            </button>
        </div>

    );

}