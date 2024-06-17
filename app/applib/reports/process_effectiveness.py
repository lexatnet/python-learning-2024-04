from .base_report import BaseReport
from enum import StrEnum, auto
from collections import namedtuple
import pandas as pd


class DiagramType(StrEnum):
    PIE_FREQUENCY = auto()

ReportPartitionConfig = namedtuple("ReportPartitionConfig", ["title", "handler", "params"])

class ProcessEffectiveness(BaseReport):

    @property
    def report_partitions_configs(self):
        return [
            ReportPartitionConfig(
                title="своевременность оказания услуги",
                handler=self.timeliness_of_service_provision,
                params=dict(),
            ),
        ]

    def timeliness_of_service_provision(self):
        """своевременность оказания услуги"""
        columns = [
            "Документ.Номер",
            "Документ.Дата",
            "Документ.Дата разрешения",
            "Документ.СЛА",
        ]
        
        data = self.strip_data_columns(columns).drop_duplicates().dropna()

        print(data.head())

        datetime_format = "%d.%m.%Y %H:%M:%S"
        data["Документ.Дата(Datetime)"] = pd.to_datetime(data["Документ.Дата"], format=datetime_format)
        data["Документ.Дата разрешения(Datetime)"] = pd.to_datetime(data["Документ.Дата разрешения"], format=datetime_format)
        data["Документ.СЛА(Datetime)"] = pd.to_datetime(data["Документ.СЛА"], format=datetime_format)
        data["Нормированный срок обработки"] = data["Документ.СЛА(Datetime)"] - data["Документ.Дата(Datetime)"]
        data["Фактический срок обработки"] = data["Документ.Дата разрешения(Datetime)"] - data["Документ.Дата(Datetime)"]
        print(data.head())

        return None

    def get_partition_context(self, config):
        return config.handler(**config.params)

    def get_context(self):
        context = dict()
        context["partitions"] = [
            self.get_partition_context(partition_config)
            for partition_config in self.report_partitions_configs
        ]
        return context
