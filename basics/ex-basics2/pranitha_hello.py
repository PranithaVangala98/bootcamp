from rich import print


def say_hello(word="World"):
    print(f"Hello [bold magenta]{word}[/bold magenta]")


if __name__ == "__main__":
    say_hello("Pranitha")
