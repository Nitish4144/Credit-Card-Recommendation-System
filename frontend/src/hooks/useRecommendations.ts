import { useEffect, useState } from "react";

import { getRecommendation } from "../services/RecommendationApi";
import { Recommendation } from "../types/Recommendation";

export function useRecommendation() {
     
    const [recommendation, setRecommendation] = useState<Recommendation[]>([]);
    console.log("Hook running");

      useEffect(() => {loadRecommendations();}, []);

    async function loadRecommendations(){
        try{
            const data = 
            await getRecommendation();
            setRecommendation(data);
        } catch(error){
            console.error(
                "Failed to fetch recommendations",
                error
            );
        }
    }
    return recommendation;
}