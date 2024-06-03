from collections import namedtuple
from .base_report import BaseReport
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import logging

logger = logging.getLogger(__name__)


class FrequencyParametersOfProcess(BaseReport):
    FILE_NAMES = {
        "request_entrance_channel": "request_entrance_channel.png",
        "entrance_classification": "entrance_classification.png",
        "mmm": "mmm.png",
    }

    def pie_chart(self, data):
        logger.debug("подготовка секторной диаграммы")
        fig, ax = plt.subplots()
        sorted_data = sorted(data, key=lambda i: i.percent, reverse=True)
        patches, texts = ax.pie([row.percent for row in sorted_data], labels=None)
        ax.legend(
            patches,
            [f"{round(row.percent, 2)} - {row.label}" for row in sorted_data],
            loc="upper left",
            bbox_to_anchor=(-0.35, 0.5),
            fontsize=8,
        )

        return fig, ax

    def render_request_entrance_channel(self, filename):
        logger.info("подготовка секторной диаграммы")
        rows_total = self.src_data.shape[0]
        data = self.src_data.groupby(
            by=["Документ.Канал"], dropna=False, as_index=False
        ).count()

        percent = lambda v: (v / rows_total) * 100

        Pie = namedtuple("Pie", ["label", "percent"])

        table = list(
            [
                Pie(label=row[1]["Документ.Канал"], percent=percent(row[1]["index"]))
                for row in data.iterrows()
            ]
        )

        fig, ax = self.pie_chart(table)
        ax.set_title("Канал поступления обращения")
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        logger.debug(f"сохранение диаграммы в файл {filename}")
        fig.savefig(filename)

    def entrance_classification(self, filename):
        rows_total = self.src_data.shape[0]
        data = self.src_data.groupby(
            by=["Документ.Классификация"], dropna=False, as_index=False
        ).count()

        percent = lambda v: (v / rows_total) * 100

        Pie = namedtuple("Pie", ["label", "percent"])

        table = list(
            [
                Pie(
                    label=row[1]["Документ.Классификация"],
                    percent=percent(row[1]["index"]),
                )
                for row in data.iterrows()
            ]
        )

        fig, ax = self.pie_chart(table)
        ax.set_title("Классификация обращения")
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(filename)

    def mmm(self, filename):
        src_columns = ["Документ.Инициатор.Организация", "Документ.Канал"]

        print(self.src_data.head())

        data = self.strip_data_columns(src_columns)
        print(data.head())
        data = (
            data
            .groupby(by=src_columns, dropna=False)
            .count()
            .unstack()
        )

        print(data.head())

    def get_context(self):
        context = dict()

        # можно значительно упростить уменьшив дублирование кода
        # context["request_entrance_channel"] = self.get_relative_file_path(
        #     "request_entrance_channel"
        # )
        # self.render_request_entrance_channel(
        #     filename=self.get_absolute_file_path("request_entrance_channel")
        # )

        # context["entrance_classification"] = self.get_relative_file_path(
        #     "entrance_classification"
        # )
        # self.entrance_classification(
        #     filename=self.get_absolute_file_path("entrance_classification")
        # )

        context["mmm"] = self.get_relative_file_path("mmm")
        self.mmm(filename=self.get_absolute_file_path("mmm"))
        return context
