import { Recommendation }
from "../types/Recommendation";

interface Props {
    recommendation: Recommendation;
    rank: number;
}

export default function RecommendationCard({
    recommendation,
    rank
}: Props) {

    return (
        <div className="recommendation-card">

            <div className="recommendation-rank">
                #{rank}
            </div>

            <div className="recommendation-name">
                {recommendation.card_name}
            </div>

            <div className="recommendation-detail">
                Reward: ₹{recommendation.reward}
            </div>

            <div className="recommendation-detail">
                Annual Fee: ₹{recommendation.annual_fee}  
            </div>

            <div className="recommendation-detail">
                Net Value: ₹{recommendation.net_value}
            </div>

            <div className="recommendation-explanation">
                {recommendation.explanation}
            </div>

        </div>
    );
}