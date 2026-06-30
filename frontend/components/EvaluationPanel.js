"use client";

import { useEffect, useState } from "react";
import { getEvaluation } from "../services/api";

export default function EvaluationPanel() {

  const [metrics, setMetrics] = useState(null);

  useEffect(() => {

    let isMounted = true;

    async function loadMetrics() {

      try {

        const data =
          await getEvaluation();

        if (isMounted) {
          setMetrics(data);
        }

      } catch (error) {

        console.error(error);

      }
    }

    loadMetrics();

    return () => {
      isMounted = false;
    };

  }, []);

  if (!metrics) {

    return (
      <div className="evaluation-card">
        Loading metrics...
      </div>
    );
  }

  return (

    <div className="evaluation-card">

      <h2>
        System Evaluation
      </h2>

      <div className="metric-grid">

        <div className="metric-box">
          <h3>Recall@K</h3>
          <p>{metrics.recall_at_k}%</p>
        </div>

        <div className="metric-box">
          <h3>Citation Coverage</h3>
          <p>{metrics.citation_coverage}%</p>
        </div>

        <div className="metric-box">
          <h3>Grounding Score</h3>
          <p>{metrics.grounding_score}%</p>
        </div>

        <div className="metric-box">
          <h3>Avg Latency</h3>
          <p>{metrics.avg_latency_ms} ms</p>
        </div>

        <div className="metric-box">
          <h3>Queries Logged</h3>
          <p>{metrics.queries_logged}</p>
        </div>

      </div>

    </div>
  );
}
