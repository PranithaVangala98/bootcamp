import typer

from dotenv import load_dotenv
from pipeline import get_processors
from core import process_lines
from typing import Optional

load_dotenv()

app = typer.Typer()


@app.command()
def run(
    input: str = typer.Option(..., "--input", "-i", help="Input filename"),
    # mode: Optional[str] = typer.Option(None, "--mode", "-m", help="Processing mode"),
    output: Optional[str] = typer.Option(
        None, "--output", "-o", help="Output filename"
    ),
    config: str = typer.Option(
        "pipeline.yaml", "--config", "-c", help="Path to YAML config file"
    ),
):
    with open(input, "r") as f:
        lines = [line.rstrip("\n") for line in f]

        processors = get_processors(config)
        result = process_lines(lines, processors)

    if output:
        with open(output, "w") as f:
            for line in result:
                f.write(line + "\n")
    else:
        for line in result:
            print(line)
