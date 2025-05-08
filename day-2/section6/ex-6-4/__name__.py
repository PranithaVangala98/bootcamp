import logging

# Create a logger named after the current module (using __name__)
logger = logging.getLogger(__name__)

# Configure logging to output to a file or stdout
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Log messages at different levels
logger.debug("This is a debug message.")
logger.info("This is an informational message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
