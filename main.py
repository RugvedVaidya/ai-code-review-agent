from fastapi import FastAPI
from app.services.review_service import analyze_repository

app = FastAPI()


@app.get("/")
def health():
    return {"status": "running"}


@app.get("/analyze")
def analyze(repo_path: str):
    return analyze_repository(repo_path)

@app.get("/analyze-github")
def analyze_github(
    repo_url: str
):
    return analyze_repository(
        repo_url=repo_url
    )
    
@app.get("/review-pr")
def review_pr(pr_url: str):
    return review_pull_request(
        pr_url
    )