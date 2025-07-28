import os
from pathlib import Path
from typing import TypedDict

from chromadb.utils import embedding_functions
from app import config


embed = embedding_functions.OpenAIEmbeddingFunction(
    api_key_env_var=config.OPENAI_API_KEY_ENV_VAR_NAME,
    model_name=config.EMBEDDING_MODEL,
)


class Document(TypedDict):
    name: str
    content: str


def load_documents(directory: Path | None = None) -> list[Document]:
    directory = directory or Path(config.DEFAULT_DOCS_DIRECTORY)
    files = [file for file in directory.glob("**/*.txt") if file.is_file()]
    documents = []
    for file in files:
        document = Document(name=file.name, content=file.read_text())
        documents.append(document)
    return documents
