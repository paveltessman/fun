from nicegui import ui, events
from fun import llm_client

from fun.rag_utils import Document


async def handle_uploaded_document(e: events.UploadEventArguments) -> None:
    document = Document(name=e.content.name, content=e.content.read().decode("utf-8"))
    await document.create_embedding()
    summary = await llm_client.get_document_summary(document.content)
    ui.markdown().set_content(summary)


@ui.page("/")
def create_pdf_inspector_page() -> None:
    ui.upload(
        label="Load your txt file", max_files=1, on_upload=handle_uploaded_document
    ).props("accept=.txt")


def start() -> None:
    create_pdf_inspector_page()
    ui.run(reload=False)
