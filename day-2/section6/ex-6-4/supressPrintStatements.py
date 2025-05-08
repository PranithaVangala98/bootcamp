import logging

# Setting up the basic configuration of the logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Creating the logger instance
logger = logging.getLogger(__name__)


def process_data():
    logger.info("Starting the data processing...")
    data = [1, 2, 3, 4, 5]
    logger.info(f"Data: {data}")

    result = sum(data)
    logger.info(f"Result: {result}")
    logger.info("Data processing completed.")


process_data()
