import json
import uuid

from embeddings.embedding_model import model

from vectordb.chroma_manager import (
    add_documents
)

CHUNKS_FILE = (
    "data/processed/chunks.json"
)


def index_chunks():

    with open(
        CHUNKS_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        chunks = json.load(f)

    ids = []
    docs = []
    metas = []
    embeddings = []

    for chunk in chunks:

        text = chunk["text"]

        embedding = model.encode(
            text
        ).tolist()

        ids.append(
            chunk["chunk_id"]
        )

        docs.append(text)

        metas.append(
            chunk["metadata"]
        )

        embeddings.append(
            embedding
        )

    add_documents(
        ids,
        embeddings,
        docs,
        metas
    )

    print(
        f"Indexed {len(ids)} chunks"
    )


def index_uploaded_chunks(chunks):

    ids = []
    docs = []
    metas = []
    embeddings = []

    for chunk in chunks:

        text = chunk["text"]

        embedding = model.encode(
            text
        ).tolist()

        ids.append(
            str(uuid.uuid4())
        )

        docs.append(text)

        metas.append(
            chunk["metadata"]
        )

        embeddings.append(
            embedding
        )

    add_documents(
        ids,
        embeddings,
        docs,
        metas
    )

    print(
        f"Indexed {len(ids)} uploaded chunks"
    )

    if docs:
        print("\n===== FIRST CHUNK =====\n")
        print(docs[0][:500])
        print("\n=======================\n")


if __name__ == "__main__":

    index_chunks()