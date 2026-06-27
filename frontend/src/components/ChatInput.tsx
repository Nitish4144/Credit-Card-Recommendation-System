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

        <div
            style={{
                display: "flex",
                gap: "10px"
            }}
        >

            <input

                value={question}

                onChange={(e) =>
                    setQuestion(e.target.value)
                }

                placeholder="Ask about credit cards..."

                style={{
                    flex: 1,
                    padding: "10px"
                }}

            />

            <button

                onClick={handleSubmit}

                disabled={loading}

            >

                {
                    loading
                        ? "Thinking..."
                        : "Send"
                }

            </button>

        </div>

    );

}