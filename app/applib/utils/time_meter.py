from datetime import datetime
from contextlib import contextmanager


@contextmanager
def time_meter_context_manager(logger, label=None):
    # Внутри вызова __enter__
    start = datetime.now()
    try:
        yield
    finally:
        # Внутри вызова __exit__
        stop = datetime.now()
        label = f"{label}: " if label else ""
        logger.debug(f"{label}Выполнение заняло {(stop-start).total_seconds()}сек.")


def time_meter_decorator(logger, label=None):
    def dec(func):
        nonlocal label
        label = label if label else func.__name__

        def wrapper(*args, **kwargs):
            start = datetime.now()
            res = func(*args, **kwargs)
            stop = datetime.now()
            logger.debug(
                f"{label}: Выполнение заняло {(stop-start).total_seconds()}сек."
            )
            return res

        return wrapper

    return dec
