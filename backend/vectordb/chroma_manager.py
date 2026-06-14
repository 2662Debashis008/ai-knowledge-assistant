import chromadb

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="knowledge_base"
)


def add_documents(
        ids,
        embeddings,
        documents,
        metadatas
):

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas
    )


def query_collection(
        embedding,
        top_k=5
):

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return results
