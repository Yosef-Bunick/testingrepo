"""Test that hello.py prints 'Hello, world!' followed by a newline."""

import subprocess
import sys


def test_hello():
    """Run hello.py as a subprocess and assert its output matches 'Hello, world!\\n'."""
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True,
        cwd=".",
    )
    expected = "Hello, world!\n"
    assert result.stdout == expected, (
        f"Expected {expected!r}, got {result.stdout!r}"
    )
    # Also check no stderr
    assert result.stderr == "", f"Unexpected stderr: {result.stderr!r}"


if __name__ == "__main__":
    test_hello()
    print("All tests passed")
