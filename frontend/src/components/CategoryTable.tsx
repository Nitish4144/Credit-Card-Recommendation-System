interface CategoryData {
    category: string;
    amount: number;
}

interface Props {
    data: CategoryData[];
}

export default function CategoryTable({
    data
}: Props) {

    return (
        <table className="category-table">

            <thead>
                <tr>
                    <th>Category</th>
                    <th>Amount</th>
                </tr>
            </thead>

            <tbody>
                {data.map((item) => (
                    <tr key={item.category}>
                        <td>{item.category}</td>
                        <td>₹{item.amount}</td>
                    </tr>
                ))}
            </tbody>

        </table>
    );
}