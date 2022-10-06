import logging
import sys
from abc import ABC


class LogMixin(ABC):

    @property
    def logger(self):
        logger: logging.Logger = logging.getLogger(f"{__name__}-{self.__class__.__name__}")
        logger.handlers.clear()
        logger.setLevel(level=logging.DEBUG)
        console = logging.StreamHandler(sys.stdout)
        logger.addHandler(console)

        return logger
