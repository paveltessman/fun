from typing import Literal

from openai.types.responses import Response
from openai import OpenAI
from app import config


def get_client() -> OpenAI:
    return OpenAI(
        api_key=config.OPENAI_API_KEY,
    )


def invoke(
    prompt: str,
    messages: list[dict[Literal["role", "content"], str]] | None = None,
    model: str | None = None,
) -> Response:
    model = model or config.CHAT_MODEL
    client = get_client()
    response = client.responses.create(
        instructions=prompt,
        input=str(messages),
        model=model,
    )
    return response
