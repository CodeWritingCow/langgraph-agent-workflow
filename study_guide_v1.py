import time
from langchain_ollama import ChatOllama

# Local Ollama model used by all three agents.
MODEL = ChatOllama(model="qwen3.5:4b", temperature=0)