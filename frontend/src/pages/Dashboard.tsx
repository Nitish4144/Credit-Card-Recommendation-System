import AnalyticsCard from "../components/AnalyticsCard";
import CategoryPieChart from "../components/CategoryPieChart";
import MonthlySpendingChart from "../components/MonthlySpendingChart";
import CategoryTable from "../components/CategoryTable";

import { useAnalytics } from "../hooks/useAnalytics";

export default function Dashboard() {

  const {
    summary,
    categories,
    monthly
  } = useAnalytics();

  if (!summary) {
    return <div>Loading...</div>;
  }

  return (
    <div className="dashboard-container">

      <h1 className="dashboard-title">
        Spending Analytics
      </h1>

      <div className="analytics-cards">

        <AnalyticsCard
          title="Total Spend"
          value={`₹${summary.total_spend}`}
        />

        <AnalyticsCard
          title="Transactions"
          value={`${summary.transaction_count}`}
        />

        <AnalyticsCard
          title="Avg Monthly Spend"
          value={`₹${summary.average_monthly_spend}`}
        />

      </div>

      <div className="charts-container">

        <div className="chart-card">
          <CategoryPieChart
            data={categories}
          />
        </div>

        <div className="chart-card">
          <MonthlySpendingChart
            data={monthly}
          />
        </div>

      </div>

      <div className="table-section">
        <CategoryTable
          data={categories}
        />
      </div>

    </div>
  );
}