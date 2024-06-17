from abc import ABC, abstractmethod
from .render import get_template
from pathlib import Path
from pandas import DataFrame
import logging

logger = logging.getLogger(__name__)

class BaseReport(ABC):
    """Базовый класс для всех отчётов"""

    def __init__(self, data: DataFrame, template_name, root_path, index="index.html"):
        self.index = index
        self.src_data = data
        self.template_name = template_name
        self.root_path = root_path

    @property
    def path(self):
        return str(Path(self.root_path).joinpath(self.index))

    @abstractmethod
    def get_context(self):
        pass

    def strip_data_columns(self, columns):
        logger.debug(f'создание нового датафрейма из колонок {columns}')
        return self.src_data.drop(
            columns=[col for col in self.src_data.columns if col not in columns]
        )

    def render(self):
        Path(self.root_path).mkdir(parents=True, exist_ok=True)
        get_template(self.template_name).stream(**self.get_context()).dump(self.path)
