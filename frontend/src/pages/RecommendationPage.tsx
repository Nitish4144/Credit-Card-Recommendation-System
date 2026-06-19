import RecommendationCard from "../components/Recommendation";
import { useRecommendation } from "../hooks/useRecommendations";

export default function RecommendationPage() {

    const recommendations = useRecommendation();

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