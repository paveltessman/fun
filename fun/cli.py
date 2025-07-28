import click
from fun import llm_client


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
