from app.services.review_service import analyze_repository

repo_path = input("Enter repository path: ")

results = analyze_repository(repo_path)

for result in results:
    print("\n====================")
    print(result["file"])
    print("====================")

    print("\nRUFF:")
    print(result["ruff"])

    print("\nBANDIT:")
    print(result["bandit"])

    print("\nLLM REVIEW:")
    print(result["review"])