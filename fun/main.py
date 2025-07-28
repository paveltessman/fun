from fun import llm_client


if __name__ == "__main__":
    response = llm_client.ask(input("Please, provide your question:\n> "))
    print(response)
