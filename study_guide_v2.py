from typing import TypedDict
import time

from langchain_ollama import ChatOllama
from langgraph import StateGraph, START, END

# Local Ollama model used by all nodes.
MODEL = ChatOllama(model="qwen3.5:4b", temperature=0)

# Shared state passed between nodes
class StudyState(TypedDict):
    topic: str
    outline: str
    notes: str
    quiz: str