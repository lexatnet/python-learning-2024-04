import matplotlib.pyplot as plt
from pathlib import Path
from collections import namedtuple
import pandas as pd
import logging
from enum import StrEnum, auto
from applib.utils.select_params import select_params_with_defaults
from .base_diagrams_report import DiagramConfig,  BaseDiagramReport

logger = logging.getLogger(__name__)

select_params = select_params_with_defaults(['title', 'filename'])

class DiagramType(StrEnum):
    PIE_FREQUENCY = auto()
    STACK_FREQUENCY = auto()


class FrequencyParametersOfProcess(BaseDiagramReport):
    @property
    def file_names(self):
        return {
            "request_entrance_channel": "request_entrance_channel.png",
            "entrance_classification": "entrance_classification.png",
            "service_request": "услуга.png",
            "service_request_by_department": "service_request_by_department.png",
            "service_request_classification_by_department": "service_request_classification_by_department.png",
        }

    @property
    def diagrams_processors(self):
        return {
            DiagramType.PIE_FREQUENCY: self.render_frequency_report_pie,
            DiagramType.STACK_FREQUENCY: self.stack_chart,
        }

    @property
    def diagrams_configs(self):
        return [
            DiagramConfig(
                type=DiagramType.PIE_FREQUENCY,
                params={"column": "Документ.Канал"},
                diagram_title="Канал поступления обращения",
                file_key="request_entrance_channel",
            ),
            DiagramConfig(
                type=DiagramType.PIE_FREQUENCY,
                params={
                    "column": "Документ.Классификация",
                },
                diagram_title="Классификация обращения",
                file_key="entrance_classification",
            ),
            DiagramConfig(
                type=DiagramType.PIE_FREQUENCY,
                params={
                    "column": "Документ.Услуга",
                },
                diagram_title="Услуга",
                file_key="service_request",
            ),
            DiagramConfig(
                type=DiagramType.STACK_FREQUENCY,
                params={
                    "columns": ["Документ.Инициатор.Организация", "Документ.Канал"],
                },
                diagram_title="Распределение каналов обращений по подразделениям",
                file_key="service_request_by_department",
            ),
            DiagramConfig(
                type=DiagramType.STACK_FREQUENCY,
                params={
                    "columns": [
                        "Документ.Инициатор.Организация",
                        "Документ.Классификация",
                    ],
                },
                diagram_title="Распределение классификаций обращений по подразделениям",
                file_key="service_request_classification_by_department",
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

    @select_params(["column"])
    def render_frequency_report_pie(
        self, filename, column, title="Частотная диаграмма"
    ):
        logger.info(f"Построение отчета анализа частотного для {column}")
        rows_total = self.src_data.shape[0]
        data = self.src_data.groupby(by=[column], dropna=False, as_index=False).count()

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

    @select_params(["columns"])
    def stack_chart(self, filename, columns, title="Стековая диаграмма"):
        logger.info(f"Построение отчета анализа частотного для {columns}")
        data = self.strip_data_columns(columns)
        data = (
            data.groupby(by=columns, dropna=False)
            .size()
            .unstack()
            .transpose()
            .fillna(0)
            .astype(int)
        )

        fig, ax = plt.subplots()
        logger.debug(f"всего на диаграмме должно быть {data.shape[1]} столбиков")
        logger.debug(f"в стеке столбика может быть до {data.shape[0]} элементов")

        width = 0.5
        bars_range = [str(i) for i in data.columns]
        print("bars_range", list(bars_range))
        bottom = pd.Series(0, index=data.columns)
        print("bottom", bottom)
        for index, row in data.iterrows():
            ax.bar(bars_range, row, width, label=str(index), bottom=bottom)
            bottom += row

        ax.set_title(title)
        ax.legend(loc="upper right")
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        logger.debug(f"сохранение диаграммы в файл {filename}")
        fig.savefig(filename)
