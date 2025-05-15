import typer
from rich import print


def main(name: str):
    print(f"Hello [bold magenta]{name}[/bold magenta]")


if __name__ == "__main__":
    typer.run(main)
