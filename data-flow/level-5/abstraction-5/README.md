## Text processing CLI tool
A modular, command-line text processing tool built with Python and [Typer](https://typer.tiangolo.com/). It reads a text file, applies a series of transformations to each line, and outputs the result either to the terminal or an output file

##  Project Structure

```
abstraction-3/
├── main.py
├── cli.py
├── core.py
├── pipeline.py         
├── types.py
├── processors/
│   ├── upper.py
│   └── snake.py
└── pipeline.yaml

```

## Features

- Fully dynamic processor loading from `pipeline.yaml`
- No hardcoded logic for mode/transformations
- Clean and pluggable architecture
-  Built with Python 3.11 and [Typer](https://typer.tiangolo.com/)
- Easily extendable with your own processors
---

##  Requirements

- Python 3.11
- [Typer](https://pypi.org/project/typer/)
- pyyaml

##  Usage

` uv run main.py --input input.txt --output output.txt  --config pipeline.yaml`

### Options
-  --input, -i: Input file path (required)

- --output, -o: Output file path (optional; prints to console if omitted)

##  Adding New Processing Modes

To add a new transformation mode:

- Open pipeline.py

- Define a new processor function via yaml

- Yaml file
 ``` pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase
```



