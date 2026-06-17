import subprocess


def run_bandit(file_path: str):
    result = subprocess.run(
        ["bandit", file_path],
        capture_output=True,
        text=True
    )

    return result.stdout if result.stdout else "No Bandit issues found."