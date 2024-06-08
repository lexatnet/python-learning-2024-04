import logging
import sys


def setup_logger(level=logging.ERROR):
    logging.basicConfig(stream=sys.stdout, level=level)
