import os
import yaml

from pathlib import Path
from typing import Optional

import logging

logger = logging.getLogger(__name__)


def _find_config_file() -> Optional[Path]:
    # 1. Check current directory
    current_dir = Path.cwd() / "_config.yaml"
    if current_dir.exists():
        logger.info("using config from current directory")
        return current_dir

    # 2. Check CONFIG_PATH environment variable
    config_paths = os.environ.get("CONFIG_PATH", "").split(":")
    for path in config_paths:
        config_path = Path(path) / "_config.yaml"
        if config_path.exists():
            logger.info("using config from CONFIG_PATH env variable")
            return config_path

    # 3. Fallback to default shipped config
    logger.info("using default config from library")
    return Path(__file__).parent / "default_config" / "_config.yaml"


def _load_config() -> dict:
    config_file = _find_config_file()
    with open(config_file, "r") as f:
        return yaml.safe_load(f)
