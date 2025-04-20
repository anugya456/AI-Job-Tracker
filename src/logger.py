
import logging
import os
from datetime import datetime
import config

def setup_logger(name):
    if not os.path.exists(config.LOGS_DIR):
        os.makedirs(config.LOGS_DIR, exist_ok=True)

    log_file = os.path.join(config.LOGS_DIR, f"{name}_{datetime.now().strftime('%Y-%m-%d')}.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
