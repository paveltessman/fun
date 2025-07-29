import asyncio
from fun import utils


async def main() -> int:
    documents = utils.load_documents()[:5]
    for document in documents:
        await document.create_embedding()
        print(f"Created embeddings for '{document.name}': {len(document.embeddings)=}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
