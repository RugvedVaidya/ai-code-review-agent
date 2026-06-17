# AI Code Review Agent

AI-powered code review tool built using:

- FastAPI
- LangChain
- Ollama
- Qwen 2.5 Coder
- Ruff
- Bandit

## Features

- Repository scanning
- Python file detection
- Static analysis using Ruff
- Security analysis using Bandit
- AI code review using local LLMs
- FastAPI API
- CLI support

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