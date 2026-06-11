import { useState } from "react";

import{
    getHealth,
    createTransaction
} from "./services/api"

function App() {
    const [result, setResult] = useState("");

    const handleHealth = async () => {
        const data = await getHealth();
        setResult(JSON.stringify(data));
    };
    const handleTransaction = async () => {
        const data = await createTransaction();
        setResult(JSON.stringify(data));
    };

    return (
        <div> 
            <h1> Credit Card Recommender</h1>

            <button onClick={handleHealth}>
                Health Check
            </button>

            <button onClick={handleTransaction}>
                Send Transaction
            </button>

            <pre>{result}</pre>
        </div>
    );
}


export default App