const API_BASE_URL = "http://localhost:8000";

export async function getHealth() { 
    const response = await fetch(
        `${API_BASE_URL}/health`
    );

return response.json();
}

export async function createTransaction() {
    const response = await fetch(
        `${API_BASE_URL}/transactions`,
        {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                merchant: "Amazon",
                amount: 500,
                category: "Shopping"
            })
        }
    );
    return response.json();
    
}