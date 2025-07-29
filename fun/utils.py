from dataclasses import dataclass
from pathlib import Path

from chromadb.utils import embedding_functions
from fun import config


embed = embedding_functions.OpenAIEmbeddingFunction(
    api_key_env_var=config.OPENAI_API_KEY_ENV_VAR_NAME,
    model_name=config.EMBEDDING_MODEL,
)


@dataclass
class Chunk:
    index: int
    content: str


@dataclass
class Document:
    name: str
    content: str
    chunks: list[Chunk]


def load_documents(directory: Path | None = None) -> list[Document]:
    directory = directory or Path(config.DEFAULT_DOCS_DIRECTORY)
    files = [file for file in directory.glob("**/*.txt") if file.is_file()]
    documents = []
    for file in files:
        content = file.read_text()
        chunks = split_text_to_chunks(content)
        document = Document(name=file.name, content=content, chunks=chunks)
        documents.append(document)
    return documents


def split_text_to_chunks(
    text: str, *, chunk_size: int | None = None, overlap: int | None = None
) -> list[Chunk]:
    chunk_size = chunk_size or config.DEFAULT_CHUNK_SIZE
    overlap = overlap or config.DEFAULT_CHUNK_OVERLAP
    chunks = []
    chunk_start = 0
    index = 0
    while chunk_start < len(text):
        chunk_end = chunk_start + chunk_size
        chunk = Chunk(index=index, content=text[chunk_start:chunk_end])
        chunks.append(chunk)
        chunk_start = chunk_end - overlap
        index += 1
    return chunks
