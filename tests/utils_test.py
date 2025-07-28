from fun import utils


def test_load_documents() -> None:
    documents = utils.load_documents()
    assert len(documents) == 21
