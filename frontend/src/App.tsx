// import { useState } from "react";
// import Dashboard from "./pages/Dashboard";
// import RecommendationsPage from "./pages/RecommendationPage";

// import {
//   getHealth,
//   createTransaction,
// } from "./services/api";

// import UploadForm from "./components/UploadForm";

// function App() {
//   const [result, setResult] = useState("");

//   const handleHealth = async () => {
//     const data = await getHealth();
//     setResult(JSON.stringify(data));
//   };

//   const handleTransaction = async () => {
//     const data = await createTransaction();
//     setResult(JSON.stringify(data));
//   };

//   return (
//     <div>
//       <h1>Credit Card Recommender</h1>

//         <button onClick={handleHealth}>
//             Health Check
//         </button>

//         <button onClick={handleTransaction}>
//             Send Transaction
//         </button>

//       <pre>{result}</pre>

//       <hr />

//          <UploadForm />
//       <hr />
//          <Dashboard />
//       <hr />
//       <RecommendationsPage />
//     </div>
    
//   );
// }

// export default App;


import UploadForm from "./components/UploadForm";
import ChatBot from "./components/ChatBot";
import Dashboard from "./pages/Dashboard";
import RecommendationsPage from "./pages/RecommendationPage";
import DeleteTransactionsButton from "./components/DeleteTransactionsButton";

function App() {
    return (
        <div
            style={{
                maxWidth: "1200px",
                margin: "0 auto",
                padding: "20px",
            }}
        >
            <h1>💳 AI Credit Card Recommendation System</h1>

            <hr />

            <UploadForm />

            <DeleteTransactionsButton />
            
            <hr />

            <Dashboard />

            <hr />

            <RecommendationsPage />

            <hr />

            <ChatBot />
        </div>
    );
}

export default App;