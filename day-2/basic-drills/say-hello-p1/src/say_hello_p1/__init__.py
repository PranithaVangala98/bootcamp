import logging
import sys
from .config_load import _load_config


logger = logging.getLogger(__name__)


def say_hello(name: str) -> str:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    config = _load_config()
    num_times = config.get("num_times", 1)
    logger.info("processing say hello")
    return " ".join([f"Hello, {name}!" for _ in range(num_times)])
