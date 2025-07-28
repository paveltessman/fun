# Fun

Just for fun. A project where I'm chilling.


## Usage

1. Clone the repo.

```bash
git clone https://github.com/paveltessman/fun.git  && cd fun
```

2. Install.

```bash
python3 -m venv .venv && source ./.venv/bin/activate && pip install -r requirements.txt && pip install -e .
```

3. Set your OpenAI API key:

```bash
echo 'OPENAI_API_KEY="<your-key-goes-here>"' > .env
```

3. Have fun.

Talk to LLM via CLI:

```bash
fun ask
```

Or run a frontend server:

```bash
fun frontend run
```


## Resources

- [OpenAI API](https://openai.com/api/).
- [Gradio](https://www.gradio.app/) for the frontend.
- [Click](https://click.palletsprojects.com/en/stable/) for CLI.
- [RAG Fundamentals and Advanced Techniques – Full Course](https://youtu.be/ea2W8IogX80) for working with documents (currently in progress).
