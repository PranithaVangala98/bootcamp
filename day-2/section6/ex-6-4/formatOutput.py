import logging

# Configuring the logger to include timestamp and severity level
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Creating the logger instance
logger = logging.getLogger(__name__)

# Logging messages at different levels
logger.debug("This is a debug message.")
logger.info("This is an informational message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
