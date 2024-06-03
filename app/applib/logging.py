import logging
import sys


def setup_logger(level=logging.ERROR):
    print("level", level)
    logging.basicConfig(stream=sys.stdout, level=level)
