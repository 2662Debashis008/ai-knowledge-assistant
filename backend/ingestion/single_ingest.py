from ingestion.parser_pdf import parse_pdf
from ingestion.parser_docx import parse_docx
from ingestion.parser_csv import parse_csv
from ingestion.parser_md import parse_md


def process_single_file(file_path):

    extension = file_path.split(".")[-1].lower()

    if extension == "pdf":
        text = parse_pdf(file_path)

    elif extension == "docx":
        text = parse_docx(file_path)

    elif extension == "csv":
        text = parse_csv(file_path)

    elif extension == "md":
        text = parse_md(file_path)

    else:
        raise Exception(
            f"Unsupported file type: {extension}"
        )

    return [
        {
            "text": text,
            "metadata": {
                "source": file_path.split("\\")[-1]
            }
        }
    ]