import typer
from say_hello_p1 import say_hello


def main(name: str):
    print(say_hello(name=name))


if __name__ == "__main__":
    typer.run(main)
