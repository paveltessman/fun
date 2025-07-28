from app import llm_client


if __name__ == "__main__":
    response = llm_client.invoke(
        prompt="You're a helpful assistant",
        messages=[
            {"role": "user", "content": "What are the capital of Great Britain?"}
        ],
    )
    print(response.output_text)
