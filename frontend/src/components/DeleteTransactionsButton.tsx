import { deleteTransactions } from "../services/api";

export default function DeleteTransactionsButton() {
    async function handleDelete() {

        const confirmed = window.confirm(
            "Delete all uploaded transactions?"
        );

        if (!confirmed) return;

        try {
            const response = await deleteTransactions();

            alert(response.message);

            window.location.reload();
        } catch (error) {
            alert("Failed to delete transactions.");
        }
    }

    return (
        <button
            onClick={handleDelete}
            style={{
                backgroundColor: "#dc2626",
                color: "white",
                border: "none",
                borderRadius: "6px",
                padding: "10px 16px",
                cursor: "pointer",
                marginBottom: "20px",
            }}
        >
            Delete All Transactions
        </button>
    );
}