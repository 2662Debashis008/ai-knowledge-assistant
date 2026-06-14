from vectordb.retriever import retrieve

results = retrieve(
    "What is KidCare?"
)

docs = results["documents"][0]
metas = results["metadatas"][0]

for i in range(len(docs)):

    print("\n")
    print("=" * 80)

    print(
        f"Source: {metas[i]['source']}"
    )

    print(
        docs[i][:300]
    )