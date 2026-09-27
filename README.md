# LangGraph Multi-Agent

A multi-agent AI system built with **LangGraph, Ollama, Qwen, and Python**. The project demonstrates how multiple specialized AI agents can collaborate through a sequential workflow to generate a structured study guide.

The system uses three specialized agents:

* **Planner** — Breaks a topic into logical study sections.
* **Teacher** — Generates concise study notes based on the outline.
* **Quiz Writer** — Creates review questions based on the study notes.

The project is based on the freeCodeCamp tutorial [How to Build Your First Multi-Agent AI System in Python and LangGraph](https://www.freecodecamp.org/news/how-to-build-your-first-multi-agent-ai-system-in-python-and-langgraph/) by Darsh Shah. The tutorial demonstrates both a plain Python implementation and a LangGraph implementation of the same multi-agent workflow.

## Architecture

The LangGraph implementation models the multi-agent workflow as a graph with shared state:

```text
START
  │
  ▼
Planner
  │
  ▼
Teacher
  │
  ▼
Quiz Writer
  │
  ▼
 END
```

Each agent is implemented as a LangGraph node. The nodes read from and update a shared state object as the workflow progresses.

The workflow follows the sequence:

1. The **Planner** receives a study topic and creates a three-section outline.
2. The **Teacher** uses the outline to generate beginner-friendly study notes.
3. The **Quiz Writer** uses the notes to generate three review questions.
4. The final state contains the complete study guide.

## Technologies

* **Python 3.12+**
* **LangGraph** — Multi-agent workflow orchestration
* **LangChain Ollama** — Integration with local Ollama models
* **Ollama** — Local LLM runtime
* **Qwen** — Local language model

## Prerequisites

Before running the project, install:

* Python 3.12 or later
* [Ollama](https://ollama.com/)
* Qwen 3.5 4B model

Pull the Qwen model with:

```bash
ollama pull qwen3.5:4b
```

## Installation

### Using Python `venv`

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

### Using Conda

Create a new Conda environment:

```bash
conda create -n langgraph-multi-agent python=3.12
conda activate langgraph-multi-agent
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Usage

This repository contains two implementations of the same multi-agent study guide system.

### Version 1: Plain Python

`study_guide_v1.py` implements the multi-agent workflow using standard Python. Each agent is represented by a function, and the functions are called sequentially.

Run the plain Python implementation:

```bash
python study_guide_v1.py
```

Enter a study topic when prompted:

```text
Enter a study topic: Newton's laws of motion
```

The application runs the Planner, Teacher, and Quiz Writer agents sequentially and produces a study guide containing an outline, study notes, and review questions.

This version demonstrates the basic concept of coordinating multiple AI agents without using a graph-based framework.

### Version 2: LangGraph

`study_guide_v2.py` implements the same workflow using LangGraph.

Run the LangGraph implementation:

```bash
python study_guide_v2.py
```

Enter a study topic when prompted:

```text
Enter a study topic: Newton's laws of motion
```

The application represents each agent as a node in a LangGraph workflow:

```text
START → Planner → Teacher → Quiz Writer → END
```

The agents communicate through shared graph state, allowing LangGraph to manage the workflow and transitions between agents.

This version demonstrates how a graph-based framework can be used to structure and orchestrate a multi-agent system.

### Comparing the Implementations

Both versions produce the same type of study guide, but they demonstrate different approaches to building the workflow:

| Implementation      | Approach     | Purpose                                      |
| ------------------- | ------------ | -------------------------------------------- |
| `study_guide_v1.py` | Plain Python | Demonstrates basic multi-agent coordination  |
| `study_guide_v2.py` | LangGraph    | Demonstrates graph-based agent orchestration |

The plain Python implementation provides a simple foundation for understanding the workflow, while the LangGraph implementation introduces concepts such as **nodes, edges, and shared state** that can be extended to more complex agentic workflows.

## Project Structure

```text
langgraph-multi-agent/
├── study_guide_v1.py    # Plain Python implementation
├── study_guide_v2.py    # LangGraph implementation
├── requirements.txt
├── README.md
└── LICENSE
```

## Multi-Agent Workflow

This project demonstrates a **sequential pipeline**, one of several common patterns for multi-agent AI systems.

Other patterns that can be implemented with LangGraph include:

* **Parallel specialists** — Multiple agents work independently on the same input.
* **Orchestrator-subagent** — An agent delegates tasks to specialized agents.
* **Supervisor/router** — An agent determines which specialist should handle a request.
* **Human-in-the-loop** — A human reviews or approves an agent's output.
* **Review/refinement loop** — One agent generates an output while another reviews or improves it.

## Tutorial

This project is based on:

> **How to Build Your First Multi-Agent AI System in Python and LangGraph**
> Darsh Shah — freeCodeCamp

[Read the original tutorial on freeCodeCamp](https://www.freecodecamp.org/news/how-to-build-your-first-multi-agent-ai-system-in-python-and-langgraph/)

The repository is intended as a learning project based on the tutorial, with the goal of exploring local LLMs, multi-agent workflows, and LangGraph.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
