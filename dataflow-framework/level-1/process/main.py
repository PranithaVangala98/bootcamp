import os
import typer
import fileinput
from dotenv import load_dotenv, dotenv_values


load_dotenv()
defaultMode = os.getenv("MY_KEY")


def read_lines(path: str):
    data = []
    with open(path, "r") as source_file:
        for line in source_file:
            data.append(line.strip())
    return data


def transform_line(line: list, mode: str):
    result = ""

    if mode is None:
        mode = defaultMode
    if mode == "uppercase":
        result = [x.upper() for x in line]
    elif mode == "snakecase":
        result = [x.lower().replace(" ", "_") for x in line]

    return result


def write_output(result: str, outputName):
    if outputName is None:
        for i in result:
            print(i)
    else:
        with open(outputName, "w") as f:
            for line in result:
                f.write(f"{line}\n")


def main(
    input: str = typer.Option(..., "--input", "-i", help="Input filename"),
    mode: str = typer.Option(None, "--mode", help="Processing mode"),
    outfileName: str = typer.Option(None, "--output", "-o", help="Output filename"),
):
    fileData = read_lines(input)
    result = transform_line(fileData, mode)
    write_output(result, outfileName)


if __name__ == "__main__":
    typer.run(main)
