from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

def chunk_text(text):

    return splitter.split_text(text)

def chunk_documents(docs):

    all_chunks = []

    for doc in docs:

        chunks = splitter.split_text(
            doc["text"]
        )

        for chunk in chunks:

            all_chunks.append(
                {
                    "text": chunk,
                    "metadata": doc["metadata"]
                }
            )

    return all_chunks