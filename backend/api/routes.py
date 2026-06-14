from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException
from fastapi.responses import FileResponse

import shutil
import os

from models.schemas import (
    AskRequest,ExportRequest
)

from services.rag_service import (
    ask_question
)

from services.indexing_service import (
    rebuild_index
)

from services.metrics_service import (
    get_metrics
)

from services.export_service import (
    export_to_docx,
    export_to_excel,
    export_to_pdf
)

from services.file_service import (
    delete_file,
    save_file
)

from ingestion.single_ingest import (
    process_single_file
)

from ingestion.chunker import (
    chunk_documents
)

from services.indexing_service import (
    index_new_chunks
)

from services.history_service import (
    get_history
)

from services.evaluation_service import (
    evaluate_recall
)

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

@router.get("/")
def home():

    return {
        "message":
        "AI Knowledge Assistant Running"
    }


@router.post("/upload")
async def upload_file(file: UploadFile):

    try:

        filepath = save_file(file)

        docs = process_single_file(filepath)

        chunks = chunk_documents(docs)

        index_new_chunks(chunks)

        return {
            "message": "Uploaded and Indexed Successfully",
            "file": file.filename
        }

    except Exception as e:

        print("UPLOAD ERROR:")
        print(str(e))

        return {
            "error": str(e)
        }

@router.post("/ask")
def ask(
        request:
        AskRequest
):

    return ask_question(
        request.question
    )

@router.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "AI Knowledge Assistant"
    }

@router.get("/documents")
def documents():

    files = os.listdir(
        UPLOAD_DIR
    )

    return {
        "count": len(files),
        "documents": files
    }

@router.delete("/documents/{filename}")
def delete_document(filename: str):

    try:
        deleted = delete_file(
            filename
        )

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Document not found"
            )

        rebuild_index()

        return {
            "message": "Document deleted",
            "file": filename
        }

    except HTTPException:
        raise

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

@router.post("/reindex")
def reindex():

    return rebuild_index()

@router.get("/metrics")
def metrics():

    return get_metrics()

@router.get("/evaluate")
def evaluate():

    return evaluate_recall()


@router.post("/export/docx")
def export_docx(request: ExportRequest):

    file_path = export_to_docx(
        request.question,
        request.answer
    )

    return FileResponse(
        path=file_path,
        filename="answer.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

@router.post("/export/excel")
def export_excel(request: ExportRequest):

    file_path = export_to_excel(
        request.question,
        request.answer
    )

    return FileResponse(
        path=file_path,
        filename="answer.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


@router.post("/export/pdf")
def export_pdf(request: ExportRequest):

    file_path = export_to_pdf(
        request.question,
        request.answer
    )

    return FileResponse(
        path=file_path,
        filename="answer.pdf",
        media_type="application/pdf"
    )


@router.get("/history")
def history():

    return get_history()