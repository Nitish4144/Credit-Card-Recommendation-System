import { useEffect, useState } from "react";

import {
  getSummary,
  getCategories,
  getMonthly
} from "../services/analyticsApi";

export const useAnalytics = () => {     //custom hook..
  const [summary, setSummary] = useState(null);
  const [categories, setCategories] = useState([]);
  const [monthly, setMonthly] = useState([]);

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