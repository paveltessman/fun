from typing import Literal

from openai.types.responses import Response
from openai.types.embedding import Embedding
from openai import AsyncOpenAI
from fun import config


def get_client() -> AsyncOpenAI:
    return AsyncOpenAI(
        api_key=config.OPENAI_API_KEY,
    )


async def invoke(
    prompt: str,
    model: str,
    messages: list[dict[Literal["role", "content"], str]] | None = None,
) -> Response:
    async with get_client() as client:
        response = await client.responses.create(
            instructions=prompt,
            input=str(messages),
            model=model,
        )
    return response


async def ask(question: str, *, prompt: str | None = None) -> str:
    prompt = prompt or "You're a helpful assistant"
    response = await invoke(
        prompt=prompt,
        messages=[{"role": "user", "content": question}],
        model=config.CHAT_MODEL,
    )
    return response.output_text


async def get_embeddings(input_chunks: list[str]) -> list[Embedding]:
    async with get_client() as client:
        response = await client.embeddings.create(
            input=input_chunks, model="text-embedding-3-small"
        )
    return response.data
