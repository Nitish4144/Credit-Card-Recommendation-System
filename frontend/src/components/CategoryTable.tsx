
export default function CategoryTable({
  data
}: any) {
  return (
    <table className="w-full border">
      <thead>
        <tr>
          <th>Category</th>
          <th>Amount</th>
        </tr>
      </thead>

      <tbody>
        {data.map((item: any) => (
          <tr key={item.category}>
            <td>{item.category}</td>

            <td>₹{item.amount}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}