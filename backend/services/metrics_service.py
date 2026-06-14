import json

LOG_FILE = "logs/query_logs.jsonl"


def get_metrics():

    latencies = []

    grounding_scores = []

    citation_count = 0

    total = 0

    try:

        with open(
            LOG_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            for line in f:

                total += 1

                record = json.loads(
                    line
                )

                latencies.append(
                    record["latency_ms"]
                )

                grounding_scores.append(
                    record["grounding_score"]
                )

                if len(
                    record["citations"]
                ) > 0:

                    citation_count += 1

    except FileNotFoundError:

        return {
            "message":
            "No logs yet"
        }

    avg_latency = round(
        sum(latencies)
        /
        len(latencies),
        2
    )

    avg_grounding = round(
        sum(grounding_scores)
        /
        len(grounding_scores),
        2
    )

    citation_coverage = round(
        citation_count
        /
        total,
        2
    )

    return {
        "queries":
        total,

        "avg_latency_ms":
        avg_latency,

        "citation_coverage":
        citation_coverage,

        "avg_grounding":
        avg_grounding
    }