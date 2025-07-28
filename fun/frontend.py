from gradio import Interface
from fun import llm_client


app = Interface(
    fn=llm_client.ask,
    inputs=["text"],
    outputs=["text"],
)
