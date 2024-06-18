import logging

logger = logging.getLogger(__name__)


def select_params(selected_params):
    params = set(selected_params)
    logger.debug(f"создание декоратора селектора параметров с полями {selected_params}")

    def dec(func):
        logger.debug(
            f"декорирование функции селектором параметров с полями {selected_params}"
        )

        def wrapper(*args, **kwargs):
            unused_params = set(kwargs.keys()) - params
            if len(unused_params) > 0:
                logger.warn(
                    f"обнаружены неопределённые параметры {unused_params} для функции {func.__name__}"
                )
            logger.debug(f"выборка параметров {selected_params} для вызова функции")
            selected_kwargs = {key: kwargs[key] for key in params}
            return func(*args, **selected_kwargs)

        return wrapper

    return dec


def select_params_with_defaults(default_params):
    logger.debug(
        f"создание декоратора селектора параметров с полями по умолчанию {default_params}"
    )

    def wrapper(selected_params):
        params = set(default_params + selected_params)
        return select_params(params)

    return wrapper
