# pyright: reportOptionalMemberAccess=false
# pyright: reportShadowedImports=false

import logging
import os
from datetime import datetime


def setup():
    LOG_FILE_NAME = datetime.now().strftime("%H_%M_%S") + ".log"
    LOG_DIR_NAME = datetime.now().strftime("%m_%d_%Y")
    LOG_DIR_PATH = os.path.join(os.getcwd(), "logs", LOG_DIR_NAME)
    os.makedirs(LOG_DIR_PATH, exist_ok=True)
    LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, LOG_FILE_NAME)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=logging.INFO,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    )


def log(message):
    logging.info(message)
