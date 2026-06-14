from ingestion.ingest import (
    ingest_documents
)

from embeddings.embedder import (
    index_chunks,
    index_uploaded_chunks
)

def rebuild_index():

    ingest_documents()

    index_chunks()

    return {
        "message":
        "Reindex completed"
    }

def index_new_chunks(chunks):

    index_uploaded_chunks(
        chunks
    )