import logging

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format='[UserID: %(user_id)s] [Function: %(funcName)s] %(message)s'
)

# Custom LoggerAdapter to inject user_id
class ContextLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return msg, {'extra': self.extra}

def get_logger(user_id):
    return ContextLoggerAdapter(logging.getLogger(__name__), {'user_id': user_id})

def fetch_data(user_id):
    logger = get_logger(user_id)
    logger.info('Fetching data from database.')

def update_profile(user_id):
    logger = get_logger(user_id)
    logger.info('Updating user profile.')

# Example usage
fetch_data('u123')
update_profile('u123')
