import logging

logger = logging.getLogger(__name__)

def divide_numbers():
    try:
        # risky operation
        result = 10 / 0
        return result
    except ZeroDivisionError as e:
        logger.error("Failed to complete divide_numbers: %s", e)
        raise  # re-raise the same exception after logging


divide_numbers()