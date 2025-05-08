import typer
import say_hello


def main(names: list[str]):
    for name in names:
        say_hello("name")


if __name__ == "__main__":
    typer.run(main)
