import asyncio
import click
from fun import gradio_frontend as front
from fun import nicegui_frontend


@click.group()
@click.version_option(version="0.0.0")
def cli() -> None:
    """Let's chill"""


@cli.command()
def ask() -> None:
    """Ask LLM a question (no context is saved)"""
    from fun import llm_client

    question = click.prompt("Enter your question")
    answer = asyncio.run(llm_client.ask(question))
    click.echo(answer)


@cli.group()
def gradio():
    """A frontend app built with Gradio"""


@gradio.command()
def start() -> None:  # pyright: ignore[reportRedeclaration]
    """Run a simple gradio frontend and chat with LLM"""
    front.get_app().launch()


@cli.group()
def nicegui():
    """A frontend app built with NiceGUI"""


@nicegui.command()
def start() -> None:
    nicegui_frontend.start()
