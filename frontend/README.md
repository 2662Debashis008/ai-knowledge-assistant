# AI Knowledge Assistant

AI-powered RAG application built using:

- Next.js
- FastAPI
- ChromaDB
- Ollama

## Features

- PDF Upload
- DOCX Upload
- CSV Upload
- Markdown Upload
- Vector Search
- Citations
- Chat History
- Dark/Light Mode
- Export PDF/DOCX/XLSX
- Evaluation Dashboard

## Architecture

User
 ↓
Next.js Frontend
 ↓
FastAPI Backend
 ↓
Retriever
 ↓
ChromaDB
 ↓
Ollama LLM

## Run Backend

```bash
uvicorn api.main:app --reload