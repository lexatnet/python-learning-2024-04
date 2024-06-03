from enum import StrEnum
import logging


class LoggingLevel(StrEnum):
    ERROR = "error"
    INFO = "info"
    DEBUG = "debug"

    def to_logging_level(self):
        mapping = {
            "error": logging.ERROR,
            "info": logging.INFO,
            "debug": logging.DEBUG,
        }
        return mapping[self.value]
