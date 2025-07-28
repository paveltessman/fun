import chromadb

from app import config, utils


chroma_client = chromadb.PersistentClient(path=config.VECTOR_DB_PATH)

collection = chroma_client.get_or_create_collection(
    name=config.COLLECTION_NAME,
    embedding_function=utils.embed,  # pyright: ignore[reportArgumentType]
)
