from app.reviewers.llm_reviewer import review_code

sample = """
def divide(a,b):
    return a/b
"""

print(review_code(sample))