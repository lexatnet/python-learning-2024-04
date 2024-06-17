from abc import ABC, abstractmethod
from .base_report import BaseReport
from pathlib import Path
from pandas import DataFrame
import logging

logger = logging.getLogger(__name__)

class BaseReportWithArtifacts(BaseReport):
    """Базовый класс для всех отчётов"""

    @property
    def files_subfolder(self):
        """Возвращает строковое имя поддиректории в которой будут размещены файлы используемые в отчёте"""
        return "files"

    @property
    @abstractmethod
    def file_names(self):
        """Должен возвращать словарь содежащий по ключам имеда файлов используемых в отчёте"""
        return dict()

    def get_relative_file_path(self, key):
        return Path(self.files_subfolder).joinpath(self.file_names[key])

    def get_absolute_file_path(self, key):
        return str(Path(self.root_path).joinpath(self.get_relative_file_path(key)))

    def strip_data_columns(self, columns):
        return self.src_data.drop(
            columns=[col for col in self.src_data.columns if col not in columns]
        )
