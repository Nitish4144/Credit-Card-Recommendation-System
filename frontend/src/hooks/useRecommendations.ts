import { useEffect, useState } from "react";

import { getRecommendation } from "../services/RecommendationApi";
import { Recommendation } from "../types/Recommendation";

export function useRecommendation() {
     
    const [recommendations, setRecommendation] = useState<Recommendation[]>([]);
    const [loading, setLoading] = useState(true);

    console.log("Hook running");

      useEffect(() => {loadRecommendations();}, []);

    async function loadRecommendations(){
        try{
            setLoading(true);
            const data = await getRecommendation();
            setRecommendation(data);
        } catch(error){
            console.error("Failed to fetch recommendations",error);
        }
        finally {
            setLoading(false);
        }
    }
    return {recommendations,loading};
}