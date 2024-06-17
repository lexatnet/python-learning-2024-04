from .base_report_with_artifacts import BaseReportWithArtifacts
from collections import namedtuple
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

DiagramConfig = namedtuple(
    "DiagramConfig", ["params", "diagram_title", "file_key", "type"]
)

ReportPart = namedtuple("ReportPart", ["image_path", "title"])

class BaseDiagramReport(BaseReportWithArtifacts):

    @property
    @abstractmethod
    def diagrams_processors(self):
        """должен возвращать словарь функций процессоров"""
        pass

    @property
    @abstractmethod
    def diagrams_configs(self):
        """должен возвращать список конфигураций ддл диаграмм"""
        pass

    def generate_report_part(self, diagram_config):
        self.diagrams_processors[diagram_config.type](
            filename=self.get_absolute_file_path(diagram_config.file_key),
            title=diagram_config.diagram_title,
            **diagram_config.params,
        )

        return ReportPart(
            image_path=self.get_relative_file_path(diagram_config.file_key),
            title=diagram_config.diagram_title,
        )

    def get_context(self):
        context = dict()

        context["report_parts"] = [
            self.generate_report_part(diagram_config)
            for diagram_config in self.diagrams_configs
        ]
        return context
