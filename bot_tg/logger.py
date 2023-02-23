import logging
import sys
from abc import ABC


class LogMixin(ABC):

    @property
    def logger(self):
        logger: logging.Logger = logging.getLogger(f"{__name__}-{self.__class__.__name__}")
        logger.handlers.clear()
        logger.setLevel(logging.DEBUG)

        info_handler = logging.StreamHandler(sys.stdout)
        info_handler.setFormatter(logging.Formatter('INFO: %(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        info_handler.setLevel(level=logging.INFO)
        logger.addHandler(info_handler)

        warning_handler = logging.StreamHandler(sys.stdout)
        warning_handler.setFormatter(logging.Formatter('WARN: %(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        warning_handler.setLevel(level=logging.WARNING)
        logger.addHandler(warning_handler)

        return logger


# TODO think about files logging
"""
# logging_example.py

import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
"""