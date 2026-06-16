export interface SummaryData {
    total_spend: number;
    transaction_count: number;
    average_monthly_spend: number;
}

export interface CategoryData {
    category: string;
    amount: number;
}

export interface MonthlyData {
    month: string;
    amount: number;
}