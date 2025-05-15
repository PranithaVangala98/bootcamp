import logging

# Setting up the basic configuration of the logger
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Creating the logger instance
logger = logging.getLogger(__name__)

# Sample variables
user_name = "Alice"
user_id = 12345

# Logging with variables included in the message using f-string formatting
logger.debug(f"User: {user_name}, User ID: {user_id}")
logger.info(f"User {user_name} has logged in.")
logger.warning(
    f"User {user_name} attempted an action with ID {user_id} that may cause issues."
)
logger.error(f"An error occurred for user {user_name} with ID {user_id}.")
