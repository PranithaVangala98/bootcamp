import logging


# Function to configure logging based on a flag
def configure_logging(debug=False):
    # Set the logging level to DEBUG if debug flag is True, otherwise INFO
    level = logging.DEBUG if debug else logging.INFO

    # Configure the logger
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


# Call this function with debug=True to enable debug logs
debug = True  # Set this flag to control logging
configure_logging(debug)

# Creating the logger instance
logger = logging.getLogger(__name__)

# Logging messages at different levels
logger.debug("This is a debug message.")  # Will only log if debug=True
logger.info("This is an informational message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
