export async function deleteTransactions() {
    const response = await fetch(
        "http://127.0.0.1:8000/transactions",
        {
            method: "DELETE",
        }
    );

    if (!response.ok) {
        throw new Error("Failed to delete transactions.");
    }

    return response.json();
}