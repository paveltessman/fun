from chromadb.utils import embedding_functions
from app import config


embed = embedding_functions.OpenAIEmbeddingFunction(
    api_key=config.OPENAI_API_KEY, model_name=config.EMBEDDING_MODEL
)
