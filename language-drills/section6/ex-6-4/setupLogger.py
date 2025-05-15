import logging

# Setting up the basic configuration of the logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Creating the logger instance
logger = logging.getLogger(__name__)

# Logging an informational message
logger.info("This is an informational message.")
