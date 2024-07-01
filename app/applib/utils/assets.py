from pathlib import Path
from shutil import copyfile
from collections import namedtuple
import logging
from applib.logging import logging_section

logger = logging.getLogger(__name__)

root = Path(__file__).parent.parent.parent


def asset_source(path):
    return root.joinpath("assets").joinpath(path)


def asset_destination(path):
    return Path("assets").joinpath(path)


AssetConfig = namedtuple("AssetConfig", ["name", "source", "destination"])


common_assets = [
    AssetConfig(
        name="bootstrap",
        source="bootstrap.min.css",
        destination="bootstrap.min.css",
    )
]


class CommonAssets:
    def __init__(self, root) -> None:
        with logging_section(
            logger, label="Создание общих ресурсов для файлов отчетов."
        ):
            self.assets = {}
            for asset_config in common_assets:
                logger.debug(f"Обработка {asset_config.name}")
                if asset_config.name in self.assets.keys():
                    logger.warning(
                        f"Дублирование имени файла {asset_config.name}. Неверная конфигурация ресурсов."
                    )
                dest = Path(root).joinpath(asset_destination(asset_config.destination))
                src = asset_source(asset_config.source)
                dest.parent.mkdir(parents=True, exist_ok=True)
                logger.debug(f"Копирование ресурса {src} в {dest}.")
                copyfile(asset_source(asset_config.source), dest)
                logger.debug(
                    f"Занкесение ресурса в реестр {asset_config.name} в {dest}."
                )
                self.assets[asset_config.name] = dest

    def get_context(self, path):
        logger.debug(f"Генерация контекста общих ресурсов для {path}.")

        def gen_asset_path(asset_key, asset_path):
            logger.debug(f"Генерация пути для {asset_key}({asset_path}).")
            return Path(asset_path).relative_to(path, walk_up=True)

        return {
            asset_key: gen_asset_path(asset_path)
            for asset_key, asset_path in self.assets.items()
        }
