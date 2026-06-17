import subprocess

def run_pytest(test_file):

    result = subprocess.run(
        ["pytest", test_file],
        capture_output=True,
        text=True
    )

    return {
        "success": result.returncode == 0,
        "stdout": result.stdout,
        "stderr": result.stderr
    }