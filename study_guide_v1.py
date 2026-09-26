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

def planner_agent(topic: str) -> str:
    system = "You are a planner agent that creates a short outline for a study plan."
    user = f"Create 3 short study sections for the topic: {topic}"
    return run_agent("planner_agent", system, user)

def teacher_agent(topic: str, outline: str) -> str:
    system = "You are a teacher agent that writes short beginner-friendly notes using the outline created by the planner agent. Keep it concise."
    user = f"Topic: {topic}\n\nOutline:\n{outline}"
    return run_agent("teacher_agent", system, user)

def quiz_agent(topic: str, notes: str) -> str:
    system = "You are a quiz agent that writes 3 short review questions based on the notes created by the teacher agent."
    user = f"Topic: {topic}\n\nNotes:\n{notes}",
    return run_agent("quiz_agent", system, user)