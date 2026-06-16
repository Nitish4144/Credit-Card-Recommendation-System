import axios from "axios";

const API_BASE = "http://localhost:8000";

export const getSummary = async() => {
    const response = await axios.get(`${API_BASE}/analytics/summary`);

    return response.data;
};

export const getCategories = async() => {
    const response = await axios.get(`${API_BASE}/analytics/categories`);

    return response.data;
};

export const getMonthly = async() => {
    const response = await axios.get(`${API_BASE}/analytics/monthly`);

    return response.data;
};