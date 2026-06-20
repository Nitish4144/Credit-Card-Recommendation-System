import RecommendationCard from "../components/Recommendation";
import { useRecommendation } from "../hooks/useRecommendations";

export default function RecommendationPage() {

    const {recommendations,loading}  = useRecommendation();
    if (loading) {
        return (
            <div className="recommendation-page">

                <h1 className="recommendation-page-title">
                    Top Credit Card Recommendations
                </h1>

                <h2>
                    🤖 Generating AI recommendations...
                </h2>

            </div>
        );
    }
    return (
        <div className="recommendation-page">

            <h1 className="recommendation-page-title">
                Top Credit Card Recommendations
            </h1>

            {
                recommendations.map(
                    (recommendation, index) => (
                        <RecommendationCard
                            key={recommendation.card_name}
                            recommendation={recommendation}
                            rank={index + 1}
                        />
                    )
                )
            }

        </div>
    );
}