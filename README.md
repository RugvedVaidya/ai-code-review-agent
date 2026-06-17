# AI Code Review Agent

AI-powered code review tool built using:

- FastAPI
- LangChain
- Ollama
- Qwen 2.5 Coder
- Ruff
- Bandit

## Features

## Features

- Repository scanning
- GitHub repository cloning
- Ruff static analysis
- Bandit security analysis
- AI-powered code review using Ollama
- Automated pytest test generation
- Test execution and validation
- Reflection-based code fixing
- LangGraph agent workflow
- Markdown report generation

## Installation

```bash
pip install -r requirements.txt
```

Install Ollama:

https://ollama.com/download

Pull model:

```bash
ollama pull qwen2.5-coder:7b
```

Run API:

```bash
uvicorn main:app --reload
```

Run CLI:

```bash
python analyze.py
```