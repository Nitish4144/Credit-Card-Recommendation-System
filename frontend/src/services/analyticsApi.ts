import api from "./api";

export const getSummary = async () => {
    const response = await api.get("/analytics/summary");
    return response.data;
};

export const getCategories = async () => {
    const response = await api.get("/analytics/categories");
    return response.data;
};

export const getMonthly = async () => {
    const response = await api.get("/analytics/monthly");
    return response.data;
};