import os
from loguru import logger


class Logger:

    @staticmethod
    def get_logger():
        logger.add(os.getenv('LOG_PATH'), level=os.getenv('LOG_LEVEL'), format='{time} - {level} - {message}')
        