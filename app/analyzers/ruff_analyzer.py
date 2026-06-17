import subprocess


def run_ruff(file_path: str):
    result = subprocess.run(
        ["ruff", "check", file_path],
        capture_output=True,
        text=True
    )

    return result.stdout if result.stdout else "No Ruff issues found."