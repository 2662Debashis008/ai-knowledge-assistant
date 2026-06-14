from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


class ExportRequest(BaseModel):
    question: str
    answer: str