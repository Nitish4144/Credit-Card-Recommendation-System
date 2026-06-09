import { Transaction } from "../types/Transaction";
 

interface Props {
    transactions: Transaction[];
}

function TransactionTable({ transactions }: Props) {
    return (
        <table border={1}>
            <thead> 
                <tr> 
                    <th> Date</th>
                    <th> Description</th>
                    <th> Amount</th>
                    <th> Category</th>
                </tr>
            </thead>

            <tbody>
                {transactions.map((transaction) => (
                    <tr key={transaction.id}>
                        <td>{transaction.date}</td>
                        <td>{transaction.description}</td>
                        <td>{transaction.amount}</td>
                        <td>{transaction.category}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    )
}


export default TransactionTable 