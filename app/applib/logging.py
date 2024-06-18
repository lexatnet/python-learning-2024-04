import logging
import sys


def setup_logger(level=logging.ERROR):
    logging.basicConfig(stream=sys.stdout, level=level)
    logging.getLogger("matplotlib").setLevel(logging.WARNING)
    logging.getLogger('PIL').setLevel(logging.INFO)
