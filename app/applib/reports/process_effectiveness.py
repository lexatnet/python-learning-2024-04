from .base_report import BaseReport
from enum import StrEnum, auto
from collections import namedtuple
import pandas as pd
from datetime import timedelta

from applib.utils.select_params import select_params_with_defaults

select_params = select_params_with_defaults(["title"])


class DiagramType(StrEnum):
    PIE_FREQUENCY = auto()


ReportPartitionConfig = namedtuple("ReportPartitionConfig", ["handler", "params"])

ReportPartition = namedtuple("ReportPartition", ["title", "type", "data"])


def criteria_by_delay_level(row):
    if row["Просрочка"].to_pytimedelta() < timedelta(0):
        return "нет просрочки"
    elif row["Просрочка"].to_pytimedelta() < timedelta(days=1):
        return "день"
    elif timedelta(days=1) < row["Просрочка"].to_pytimedelta() < timedelta(days=7):
        return "неделя"
    elif timedelta(days=7) < row["Просрочка"].to_pytimedelta() < timedelta(days=30):
        return "месяц"
    return "большая"


class ProcessEffectiveness(BaseReport):

    @property
    def report_partitions_configs(self):
        return [
            ReportPartitionConfig(
                handler=self.timeliness_of_service_provision,
                params={
                    "title": "своевременность оказания услуги",
                },
            ),
            ReportPartitionConfig(
                handler=self.timeliness_of_service_provision_by_reciver_category,
                params={
                    "title": "своевременность оказания услуги в рамках подразделений",
                    "column": "Документ.Площадка.Категория площадки",
                },
            ),
        ]

    @select_params([])
    def timeliness_of_service_provision(self, title):
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
        data["Документ.Дата(Datetime)"] = pd.to_datetime(
            data["Документ.Дата"], format=datetime_format
        )
        data["Документ.Дата разрешения(Datetime)"] = pd.to_datetime(
            data["Документ.Дата разрешения"], format=datetime_format
        )
        data["Документ.СЛА(Datetime)"] = pd.to_datetime(
            data["Документ.СЛА"], format=datetime_format
        )
        data["Нормированный срок обработки"] = (
            data["Документ.СЛА(Datetime)"] - data["Документ.Дата(Datetime)"]
        )
        data["Фактический срок обработки"] = (
            data["Документ.Дата разрешения(Datetime)"] - data["Документ.Дата(Datetime)"]
        )
        print(data.head())

        data["Просрочка"] = (
            data["Документ.Дата разрешения(Datetime)"] - data["Документ.СЛА(Datetime)"]
        )

        print(data.head())

        data["Категория Просрочки"] = data.apply(
            criteria_by_delay_level, axis="columns"
        )

        docs_total_count = data.shape[0]

        res = data.groupby(by=["Категория Просрочки"]).size()  # возвращается серия
        print(res.head())
        res_percent = (res / docs_total_count) * 100  # гернерируется серия
        print(res_percent.head())

        return ReportPartition(title=title, type="table", data=res_percent)

    @select_params(["column"])
    def timeliness_of_service_provision_by_reciver_category(self, title, column):
        """своевременность оказания услуги по категории места обшращения"""
        columns = [
            "Документ.Номер",
            "Документ.Дата",
            "Документ.Дата разрешения",
            "Документ.СЛА",
            column,
        ]

        data = self.strip_data_columns(columns).drop_duplicates().dropna()

        print(data.head())

        datetime_format = "%d.%m.%Y %H:%M:%S"
        data["Документ.Дата(Datetime)"] = pd.to_datetime(
            data["Документ.Дата"], format=datetime_format
        )
        data["Документ.Дата разрешения(Datetime)"] = pd.to_datetime(
            data["Документ.Дата разрешения"], format=datetime_format
        )
        data["Документ.СЛА(Datetime)"] = pd.to_datetime(
            data["Документ.СЛА"], format=datetime_format
        )
        data["Нормированный срок обработки"] = (
            data["Документ.СЛА(Datetime)"] - data["Документ.Дата(Datetime)"]
        )
        data["Фактический срок обработки"] = (
            data["Документ.Дата разрешения(Datetime)"] - data["Документ.Дата(Datetime)"]
        )
        print(data.head())

        data["Просрочка"] = (
            data["Документ.Дата разрешения(Datetime)"] - data["Документ.СЛА(Datetime)"]
        )

        print(data.head())

        data["Категория Просрочки"] = data.apply(
            criteria_by_delay_level, axis="columns"
        )

        docs_total_count = data.shape[0]

        res = data.groupby(
            by=[column, "Категория Просрочки"]
        ).size()  # возвращается серия
        print(res)

        for i in res.index:
            print(i)
            print(res[i])

        print(res.unstack())

        return ReportPartition(title=title, type="table", data=res)

    def get_partition_context(self, config):
        return config.handler(**config.params)

    def get_context(self):
        context = super().get_context()
        context["partitions"] = [
            self.get_partition_context(partition_config)
            for partition_config in self.report_partitions_configs
        ]
        return context
