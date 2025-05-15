# main.py
import os
import logging
from cli import app  # cli.py will now handle the Typer app definition

# Configure basic logging
# The log level can be overridden by the --debug flag in cli.py
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    """
    Main entry point for the application.
    It calls the Typer application defined in cli.py.
    """
    # Example: Set an environment variable if it's not already set.
    # This is just to show how main.py can be used for setup before CLI takes over.
    # os.environ.setdefault('MY_APP_DEFAULT_SETTING', 'some_value')

    # The Typer app in cli.py will parse arguments and execute commands.
    # If --debug is passed, cli.py will update the logging level.
    app()


if __name__ == "__main__":
    logger.info("Application starting...")
    main()
    logger.info("Application finished.")
