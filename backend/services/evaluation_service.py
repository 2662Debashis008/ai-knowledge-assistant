import json

from vectordb.retriever import retrieve


def calculate_grounding(
        answer,
        docs
):

    answer_words = set(
        answer.lower().split()
    )

    context_words = set(
        " ".join(docs)
        .lower()
        .split()
    )

    overlap = answer_words.intersection(
        context_words
    )

    score = round(
        len(overlap)
        /
        max(len(answer_words), 1),
        2
    )

    return score

def evaluate_recall():

    with open(
        "evaluation/questions.json",
        "r",
        encoding="utf-8"
    ) as f:

        dataset = json.load(f)

    hits = 0

    total = len(dataset)

    for item in dataset:

        results = retrieve(
            item["question"],
            top_k=5
        )

        metas = results["metadatas"][0]

        found = False

        for meta in metas:

            if (
                meta["source"]
                ==
                item["expected_source"]
            ):
                found = True
                break

        if found:
            hits += 1

    recall = round(
        hits / total,
        2
    )

    return {
        "recall_at_5":
        recall,

        "hits":
        hits,

        "total":
        total
    }