from collections import namedtuple
from .base_report import BaseReport
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np


class FrequencyParametersOfProcess(BaseReport):
    FILE_NAMES = {"request_entrance_channel": "request_entrance_channel.png"}

    def pie_chart(self, data):
        fig, ax = plt.subplots()
        sorted_data = sorted(data, key=lambda i: i.percent, reverse=True)
        patches, texts = ax.pie([row.percent for row in sorted_data], labels=None)
        ax.legend(
            patches, 
            [f"{round(row.percent, 2)} - {row.label}" for row in sorted_data], 
            loc='upper left',
            bbox_to_anchor=(-0.35, .5),
            fontsize=8
        )

        return fig, ax


    def render_request_entrance_channel(self, filename):
        rows_total = self.src_data.shape[0]
        data = self.src_data.groupby(
            by=["Документ.Канал"], dropna=False, as_index=False
        ).count()

        percent = lambda v : ( v / rows_total ) * 100

        Pie = namedtuple('Pie', ['label', 'percent'])

        table = list([
            Pie(
                label=row[1]["Документ.Канал"],
                percent=percent(row[1]['index'])
            ) for row in data.iterrows()
        ])

        fig, ax = self.pie_chart(table)
        ax.set_title("Канал поступления обращения")
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(filename)

    def get_context(self):
        context = dict() 
        context["request_entrance_channel"] = self.get_relative_file_path(
            "request_entrance_channel"
        )
        self.render_request_entrance_channel(
            filename=self.get_absolute_file_path("request_entrance_channel")
        )
        return context
