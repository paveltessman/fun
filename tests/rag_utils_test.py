from fun import rag_utils
from fun.rag_utils import Chunk


def test_load_documents() -> None:
    documents = rag_utils.load_documents()
    assert len(documents) == 21


def test_split_text_to_chunks() -> None:
    text = "abcdefghijkl"
    chunks = rag_utils.split_text_to_chunks(text, chunk_size=4, overlap=1)
    expected_chunks = [
        Chunk(index=0, content="abcd"),
        Chunk(index=1, content="defg"),
        Chunk(index=2, content="ghij"),
        Chunk(index=3, content="jkl"),
    ]
    assert chunks == expected_chunks
