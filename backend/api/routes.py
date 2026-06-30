from fastapi import APIRouter
from fastapi import UploadFile
from fastapi.responses import FileResponse

import os

from models.schemas import (
    AskRequest,
    ExportRequest
)

from services.rag_service import (
    ask_question
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
    get_history,
    delete_chat,
    create_chat
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


# ---------------- HOME ---------------- #

@router.get("/")
def home():

    return {
        "message":
        "AI Knowledge Assistant Running"
    }


# ---------------- UPLOAD ---------------- #

@router.post("/upload")
async def upload_file(file: UploadFile):

    try:

        filepath = save_file(file)

        docs = process_single_file(filepath)

        chunks = chunk_documents(docs)

        index_new_chunks(chunks)

        return {
            "message":
            "Uploaded and Indexed Successfully",
            "file":
            file.filename
        }

    except Exception as e:

        return {
            "error":
            str(e)
        }


# ---------------- ASK ---------------- #

@router.post("/ask")
def ask(request: AskRequest):

    return ask_question(
        request.question,
        request.chat_id
    )

#---------------Create New Chat -----------#

@router.post("/new-chat")
def new_chat():

    return create_chat()

# ---------------- HEALTH ---------------- #

@router.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "AI Knowledge Assistant"
    }


# ---------------- DOCUMENTS ---------------- #

@router.get("/documents")
def documents():

    files = os.listdir(
        UPLOAD_DIR
    )

    return {
        "count": len(files),
        "documents": files
    }


# ---------------- METRICS ---------------- #

@router.get("/metrics")
def metrics():

    return get_metrics()


# ---------------- EVALUATION ---------------- #

@router.get("/evaluate")
def evaluate():

    return evaluate_recall()


# ---------------- HISTORY ---------------- #

@router.get("/history")
def history():

    return get_history()


# ---------------- DELETE CHAT ---------------- #

@router.delete("/history/{chat_id}")
def delete_history(chat_id: str):

    return delete_chat(chat_id)

# ---------------- EXPORT DOCX ---------------- #

@router.post("/export/docx")
def export_docx(
    request: ExportRequest
):

    file_path = export_to_docx(
        request.question,
        request.answer
    )

    return FileResponse(
        path=file_path,
        filename="answer.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )


# ---------------- EXPORT EXCEL ---------------- #

@router.post("/export/excel")
def export_excel(
    request: ExportRequest
):

    file_path = export_to_excel(
        request.question,
        request.answer
    )

    return FileResponse(
        path=file_path,
        filename="answer.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


# ---------------- EXPORT PDF ---------------- #

@router.post("/export/pdf")
def export_pdf(
    request: ExportRequest
):

    file_path = export_to_pdf(
        request.question,
        request.answer
    )

    return FileResponse(
        path=file_path,
        filename="answer.pdf",
        media_type="application/pdf"
    )