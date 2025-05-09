# CLI Text Transformer

A simple command-line tool that reads lines from a text file, transforms each line according to a specified mode, and outputs the result either to stdout or to an output file.

## Features
- **uppercase**: Convert each line to uppercase.
- **snakecase**: Convert each line to lowercase and replace spaces with underscores.
- Reads input from a file.
- Outputs results to console or writes to a file.
- Configurable default mode via environment variable.

---

## Prerequisites
- Python 3.11 or higher
- `typer` library for CLI interface
- `python-dotenv` for loading environment variables

## Installation

1. Clone the repository or copy the script to your project directory.
2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   
   ```

## Environment variables

MY_KEY: Sets the default transformation mode if --mode is not provided. Valid values:

- uppercase

- snakecase


## Usage

` python transform.py --input <input_file> [--mode <mode>] [--output <output_file>] `

### Options
- -i, --input : (Required) Path to the input text file.

- --mode : Transformation mode (uppercase or snakecase). Defaults to MY_KEY from .env if not provided.

- -o, --output : Path to save the transformed output. If omitted, prints to console.