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

  if (!summary)
    return <div>Loading...</div>;

  return (
    <div className="p-8">

      <h1 className="text-3xl font-bold mb-6">
        Spending Analytics
      </h1>

      <div className="grid grid-cols-3 gap-4 mb-8">

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

      <div className="grid grid-cols-2 gap-8">
 
         <CategoryPieChart
          data={categories}
          />
         
        <MonthlySpendingChart
          data={monthly}
        /> 
        
          {/* <div>Pie Chart Test</div> */}

          {/* <div>Monthly Chart Test</div> */}

      </div>

      <div className="mt-8">
        <CategoryTable
          data={categories}
        />
      </div>

    </div>
  );
}