from embeddings.embedding_model import model

from vectordb.chroma_manager import (
    query_collection
)

def retrieve(query, top_k=5):

    query_embedding = model.encode(
        query
    ).tolist()

    results = query_collection(
        query_embedding,
        top_k=1
    )

    print("\n=========== QUERY ===========")
    print(query)

    print("\n=========== DOCUMENTS ===========")

    for doc in results["documents"][0]:
        print(doc[:500])
        print("\n-----------------\n")

    return results