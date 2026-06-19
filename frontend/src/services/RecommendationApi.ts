import axios from "axios";

const API_BASE = "http://localhost:8000";

export async function getRecommendation() {

        console.log("Calling recommendations API");

    const response = await axios.get(`${API_BASE}/recommendations`);
    return response.data;
}