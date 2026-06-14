import os
import json

from ingestion.parser_pdf import parse_pdf
from ingestion.parser_docx import parse_docx
from ingestion.parser_csv import parse_csv
from ingestion.parser_md import parse_md

from ingestion.chunker import chunk_text


UPLOAD_DIR = "uploads"

OUTPUT_FILE = (
    "data/processed/chunks.json"
)


def parse_document(file_path):

    extension = (
        file_path.split(".")[-1]
        .lower()
    )

    if extension == "pdf":
        return parse_pdf(file_path)

    elif extension == "docx":
        return parse_docx(file_path)

    elif extension == "csv":
        return parse_csv(file_path)

    elif extension == "md":
        return parse_md(file_path)

    return ""


def ingest_documents():

    all_chunks = []

    for file_name in os.listdir(
        UPLOAD_DIR
    ):

        file_path = os.path.join(
            UPLOAD_DIR,
            file_name
        )

        text = parse_document(
            file_path
        )

        chunks = chunk_text(text)

        for idx, chunk in enumerate(
            chunks
        ):

            all_chunks.append(
                {
                    "chunk_id":
                    f"{file_name}_{idx}",

                    "text":
                    chunk,

                    "metadata":
                    {
                        "source":
                        file_name,

                        "chunk":
                        idx
                    }
                }
            )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            all_chunks,
            f,
            indent=4
        )

    print(
        f"Created {len(all_chunks)} chunks"
    )


if __name__ == "__main__":
    ingest_documents()