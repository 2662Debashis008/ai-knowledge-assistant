from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME")

DATABASE_URL = os.getenv("DATABASE_URL")

CHROMA_PATH = os.getenv("CHROMA_PATH")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")