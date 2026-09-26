import time
from langchain_ollama import ChatOllama

# Local Ollama model used by all three agents.
MODEL = ChatOllama(model="qwen3.5:4b", temperature=0)

def ask(system: str, user: str) -> str:
    """Run one LLM call with a system prompt and user input."""
    response = MODEL.chat([
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ])
    return response.content

def run_agent(name: str, system: str, user: str) -> str:
    """Helper that runs an agent and logs how long it takes."""
    print(f"Calling agent {name}...")
    start = time.time()
    result = ask(system, user)
    print(f"Finished running '{name}' in {time.time() - start:.2f} seconds.")
    return result