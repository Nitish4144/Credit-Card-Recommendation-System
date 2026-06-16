import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

export default function MonthlySpendingChart({data}: any) {
  return (
    <LineChart
      width={700}
      height={300}
      data={data}
    >
      <CartesianGrid strokeDasharray="3 3" />

      <XAxis dataKey="month" />

      <YAxis />

      <Tooltip />

      <Line
        type="monotone"
        dataKey="amount"
      />
    </LineChart>
  );
}