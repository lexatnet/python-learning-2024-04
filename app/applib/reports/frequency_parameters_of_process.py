from collections import namedtuple
from .base_report import BaseReport
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import logging

logger = logging.getLogger(__name__)

DiagramConfig = namedtuple("DiagramConfig", ["column", "diagram_title", "file_key"])

class FrequencyParametersOfProcess(BaseReport):
    FILE_NAMES = {
        "request_entrance_channel": "request_entrance_channel.png",
        "entrance_classification": "entrance_classification.png",
        "service_request": "услуга.png",
        "mmm": "mmm.png",
    }

    FREQUENCY_DIAGRAMS = [
        DiagramConfig(
            column="Документ.Канал",
            diagram_title="Канал поступления обращения",
            file_key="request_entrance_channel",
        ),
        DiagramConfig(
            column="Документ.Классификация",
            diagram_title="Классификация обращения",
            file_key="entrance_classification",
        ),
        DiagramConfig(
            column="Документ.Услуга",
            diagram_title="Услуга",
            file_key="service_request",
        ),
    ]

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
    
    

    def render_frequency_report_pie(self, filename, column, title = 'Частотная диаграмма'):
        logger.info(f"построете отчета анализа чатотного для {column}")
        rows_total = self.src_data.shape[0]
        data = self.src_data.groupby(
            by=[column], dropna=False, as_index=False
        ).count()

        percent = lambda v: (v / rows_total) * 100

        Pie = namedtuple("Pie", ["label", "percent"])

        table = list(
            [
                Pie(label=row[1][column], percent=percent(row[1]["index"]))
                for row in data.iterrows()
            ]
        )

        fig, ax = self.pie_chart(table)
        ax.set_title(title)
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        logger.debug(f"сохранение диаграммы в файл {filename}")
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
        )

        print('grouped', data.head())
        data = data.unstack()
        print(data.head())


    def get_context(self):
        context = dict()

        for diagram_config in self.FREQUENCY_DIAGRAMS:
            context[diagram_config.file_key] = self.get_relative_file_path(
                diagram_config.file_key
            )
            self.render_frequency_report_pie(
                filename=self.get_absolute_file_path(diagram_config.file_key),
                column=diagram_config.column,
                title = diagram_config.diagram_title
            )

        # context["mmm"] = self.get_relative_file_path("mmm")
        # self.mmm(filename=self.get_absolute_file_path("mmm"))
        return context
