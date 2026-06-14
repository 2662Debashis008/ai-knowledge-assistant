import json

from vectordb.retriever import retrieve

def evaluate_recall():

    tests = json.load(
        open(
            "evaluation/eval_set.json"
        )
    )

    correct = 0

    for test in tests:

        results = retrieve(
            test["question"],
            top_k=5
        )

        sources = [

            m["source"]

            for m in
            results["metadatas"][0]
        ]

        if test["expected_source"] in sources:

            correct += 1

    recall = correct / len(tests)

    return recall