import asyncio
import click
from fun import gradio_frontend as front


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
def start() -> None:
    """Run a simple gradio frontend and chat with LLM"""
    front.get_app().launch()
