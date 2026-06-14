# Hello World — Python Project

A minimal Python project that prints "Hello, world!" and validates it via a test.

## Project Structure

```
hello_test/
├── hello.py          # Prints "Hello, world!"
├── test_hello.py     # Subprocess-based test for hello.py
├── README.md         # This file
├── TODO.md           # Task checklist
├── CHANGELOG.md      # Version history
└── PATTERNS.md       # Architecture & conventions
```

## How to Run

### Run the hello script directly

```bash
python hello.py
```

Expected output:

```
Hello, world!
```

### Run the test suite

```bash
python -m pytest test_hello.py -v
```

Or run the test file directly:

```bash
python test_hello.py
```

Expected output on success:

```
All tests passed
```

## Requirements

- Python 3.6+ (uses `subprocess.run` with `capture_output=True` and `text=True`)
- No third-party packages required (stdlib only)

## Quick Start

```bash
# Run the program
python hello.py

# Run the test
python test_hello.py
```
