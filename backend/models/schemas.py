from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str
    chat_id: str

class ExportRequest(BaseModel):
    question: str
    answer: str