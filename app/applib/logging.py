import logging
import sys
from contextlib import contextmanager


def setup_logger(level=logging.ERROR):
    logging.basicConfig(stream=sys.stdout, level=level)
    logging.getLogger("matplotlib").setLevel(logging.WARNING)
    logging.getLogger("PIL").setLevel(logging.INFO)


@contextmanager
def logging_section(logger, level="debug", label="Секция логирования", params=None):
    # Внутри вызова __enter__
    func = getattr(logger, level)
    func(f"начало:{label}")
    if params:
        func(f"параметры:{params}")
    try:
        yield
    finally:
        # Внутри вызова __exit__
        func(f"конец:{label}")
