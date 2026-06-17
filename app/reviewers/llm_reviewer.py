from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5-coder:7b"
)


def review_code(code: str):
    prompt = f"""
You are a senior software engineer.

Review this code and identify:

- Bugs
- Security issues
- Performance concerns
- Readability problems
- Missing edge cases

Provide actionable suggestions.

Code:
{code}
"""

    response = llm.invoke(prompt)

    return response.content