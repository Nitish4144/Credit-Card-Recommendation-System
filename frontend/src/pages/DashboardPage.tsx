import UploadForm from "../components/UploadForm";
import ChatBot from "../components/ChatBot";
import Dashboard from "./Dashboard";
import RecommendationsPage from "./RecommendationPage";
import DeleteTransactionsButton from "../components/DeleteTransactionsButton";

export default function DashboardPage() {
    return (
        <div
            style={{
                maxWidth: "1200px",
                margin: "0 auto",
                padding: "20px",
                background: "#121212",
                color: "#ffffff"
            }}
        >
            <h1>AI Credit Card Recommendation System</h1>

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