// export async function deleteTransactions() {
//     const response = await fetch(
//         "http://127.0.0.1:8000/transactions",
//         {
//             method: "DELETE",
//         }
//     );

//     if (!response.ok) {
//         throw new Error("Failed to delete transactions.");
//     }

//     return response.json();
// }

import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

api.interceptors.request.use((config) => {
    const token = localStorage.getItem("token");

    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
});

export async function deleteTransactions() {
    const response = await api.delete(
        "/transactions"
    );

    return response.data;
}

export default api;