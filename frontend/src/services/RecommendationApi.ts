import api from "./api";

export async function getRecommendation() {
    const response = await api.get("/recommendations/");
    return response.data;
}