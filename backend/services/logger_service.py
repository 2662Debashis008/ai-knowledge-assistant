import json
import os
from datetime import datetime

LOG_FILE = "logs/query_logs.json"

os.makedirs(
    "logs",
    exist_ok=True
)

def log_query(
    question,
    latency,
    chunk_ids,
    answer,
    citations,
    grounding
):

    entry = {
        "timestamp": str(
            datetime.now()
        ),
        "question": question,
        "latency_ms": latency,
        "chunk_ids": chunk_ids,
        "answer": answer,
        "citations": citations,
        "grounding": grounding
    }

    logs = []

    if os.path.exists(LOG_FILE):

        with open(
            LOG_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            try:
                logs = json.load(f)
            except:
                logs = []

    logs.append(entry)

    with open(
        LOG_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            logs,
            f,
            indent=4
        )