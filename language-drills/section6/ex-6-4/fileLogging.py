import logging

# Configuring the logger to log to a file instead of stdout
logging.basicConfig(
    filename="app.log",  # Log output will go to this file
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Creating the logger instance
logger = logging.getLogger(__name__)

# Logging messages at different levels
logger.debug("This is a debug message.")
logger.info("This is an informational message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
