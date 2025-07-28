import click
from fun import llm_client
from fun import frontend as front


@click.group()
@click.version_option(version="0.0.0")
def cli() -> None:
    """Let's chill"""


@cli.command()
def ask() -> None:
    """Ask LLM a question (no context is saved)"""
    question = click.prompt("Enter your question")
    answer = llm_client.ask(question)
    click.echo(answer)


@cli.group()
def frontend():
    """A frontend app built with Gradio"""


@frontend.command()
def start() -> None:
    """Start the frontend app where you can ask LLM questions"""
    front.app.launch()
