import { useEffect, useState } from "react";

import {
  getSummary,
  getCategories,
  getMonthly
} from "../services/analyticsApi";

import {
  SummaryData,
  CategoryData,
  MonthlyData
} from "../types/analytics";

export const useAnalytics = () => {     //custom hook..
    const [summary, setSummary] =
    useState<SummaryData | null>(null);

    const [categories, setCategories] =
    useState<CategoryData[]>([]);

    const [monthly, setMonthly] =
    useState<MonthlyData[]>([]);

  useEffect(() => {
    const loadData = async () => {
      const [
        summaryData,
        categoryData,
        monthlyData
        ] = await Promise.all([
        getSummary(),
        getCategories(),
        getMonthly()
      ]);

      setSummary(summaryData);
      setCategories(categoryData);
      setMonthly(monthlyData);
    };

    loadData();
  }, []);

  return {
    summary,
    categories,
    monthly
  };
};