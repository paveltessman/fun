from gradio import Blocks, Button, Tab, ChatInterface, File, Text
from fun import llm_client


def get_app():
    with Blocks() as app:
        with Tab("Chat"):
            chat = ChatInterface(fn=llm_client.chat, type="messages")

        with Tab("Load documents"):
            file = File()
            text = Text()
            load_button = Button("Load")
    return app
