import {
  PieChart,
  Pie,
  Tooltip,
  Cell
} from "recharts";

const COLORS = [
  "#0088FE",
  "#00C49F",
  "#FFBB28",
  "#FF8042"
];

export default function CategoryPieChart({data}: any) {
  return (
    <PieChart width={400} height={300}>
      <Pie
        data={data}
        dataKey="amount"
        nameKey="category"
        outerRadius={100}
      >
        {data.map(
          (_: any, index: number) => (
            <Cell
              key={index}
              fill={COLORS[index %COLORS.length]}
            />
          )
        )}
      </Pie>

      <Tooltip />
    </PieChart>
  );
}