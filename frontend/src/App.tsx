import UploadPage from "./components/UploadPage"
import TransactionTable from "./components/TransactionTable"
import {transactions} from "./data/transaction"


function App() {
    return (
        <div style = {{padding: "20px"}}>
            <h1> AI Credit Card Reccommendation System</h1>

            <UploadPage/>

            <hr />

            <TransactionTable transactions={transactions} />
        </div>
    );
}

export default App;