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
    model: str,
    messages: list[dict[Literal["role", "content"], str]] | None = None,
) -> Response:
    client = get_client()
    response = client.responses.create(
        instructions=prompt,
        input=str(messages),
        model=model,
    )
    return response


def ask(question: str, prompt: str | None = None) -> str:
    prompt = prompt or "You're a helpful assistant"
    response = invoke(
        prompt=prompt,
        messages=[{"role": "user", "content": question}],
        model=config.CHAT_MODEL,
    )
    return response.output_text
