from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5-coder:7b"
)

def generate_tests(code: str):

    prompt = f"""
You are a senior Python QA engineer.

Generate pytest test cases.

Return only Python code.

Code:
{code}
"""

    response = llm.invoke(prompt)

    return response.content