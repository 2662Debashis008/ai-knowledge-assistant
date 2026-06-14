import time

from vectordb.retriever import retrieve

from llm.prompt_builder import build_prompt

from llm.ollama_client import generate_answer

from services.history_service import save_chat

from services.logger_service import log_query

from services.evaluation_service import calculate_grounding


def ask_question(question):

    start_time = time.time()

    results = retrieve(
        question,
        top_k=5
    )

    docs = results["documents"][0]

    metas = results["metadatas"][0]

    chunk_ids = results["ids"][0]

    prompt = build_prompt(
        question,
        docs
    )

    answer = generate_answer(
        prompt
    )

    latency = round(
        (time.time() - start_time) * 1000,
        2
    )

    grounding = calculate_grounding(
        answer,
        docs
    )

    save_chat(
        question,
        answer
    )

    citations = []

    for meta in metas:

        citations.append(
            {
                "source":
                meta["source"]
            }
        )

    log_query(
        question,
        latency,
        chunk_ids,
        answer,
        citations,
        grounding
    )

    return {
        "answer":
        answer,

        "citations":
        citations,

        "latency_ms":
        latency,

        "grounding_score":
        grounding,

        "chunk_ids":
        chunk_ids
    }