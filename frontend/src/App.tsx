import { useState } from "react";
import Dashboard from "./pages/Dashboard";


import {
  getHealth,
  createTransaction,
} from "./services/api";

import UploadForm from "./components/UploadForm";

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
      <h1>Credit Card Recommender</h1>

        <button onClick={handleHealth}>
            Health Check
        </button>

        <button onClick={handleTransaction}>
            Send Transaction
        </button>

      <pre>{result}</pre>

      <hr />

         <UploadForm />
      <hr />
         <Dashboard />
    </div>
    
  );
}

export default App;