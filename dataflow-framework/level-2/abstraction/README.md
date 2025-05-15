## Text processing CLI tool
A modular, command-line text processing tool built with Python and [Typer](https://typer.tiangolo.com/). It reads a text file, applies a series of transformations to each line, and outputs the result either to the terminal or an output file

##  Project Structure

```
├── main.py # Entry point of the application
├── cli.py # Handles command-line interface (Typer)
├── core.py # Applies a list of processors to input lines
├── pipeline.py # Chooses processors based on selected mode
└── types.py # Defines the ProcessorFn function type

```

## Features

- Read input from a file
- Apply transformations like:
  - `uppercase`: Converts all lines to UPPERCASE
  - `snakecase`: Converts lines to snake_case
- Environment-based default mode support using `.env`
- Output to a file or the console
- Easily extendable with new transformations

---

##  Requirements

- Python 3.11
- [Typer](https://pypi.org/project/typer/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

##  Usage

` python3 main.py run --input input.txt --mode uppercase --output output.txt`

### Options
-  --input, -i: Input file path (required)

- --mode, -m: Processing mode (optional if .env is set)

- --output, -o: Output file path (optional; prints to console if omitted)

## Environment Variables

`MY_KEY=uppercase `

If --mode is not passed at runtime, the value of MY_KEY will be used as the default mode.

##  Adding New Processing Modes

To add a new transformation mode:

- Open pipeline.py

- Define a new processor function:

## asciinema link
https://asciinema.org/connect/4441c0d5-b2da-4d1c-987d-5a1469db365d