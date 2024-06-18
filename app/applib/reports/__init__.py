from .render import get_template
from .frequency_parameters_of_process import FrequencyParametersOfProcess
from .process_effectiveness import ProcessEffectiveness
from pathlib import Path

from collections import namedtuple

ReportConfig = namedtuple(
    "ReportConfig", ["klass", "template_name", "subfolder", "title"]
)

reports = [
    ReportConfig(
        klass=FrequencyParametersOfProcess,
        template_name="frequency_parameters_of_process.html",
        subfolder="frequency_parameters_of_process",
        title="Частотные показатели процесса.",
    ),
    ReportConfig(
        klass=ProcessEffectiveness,
        template_name="process_effectiveness.html",
        subfolder="process_effectiveness",
        title="Результативность процесса.",
    ),
]


def create_reports(data, destination):
    Path(destination).mkdir(parents=True, exist_ok=True)
    index_path = str(Path(destination).joinpath("index.html"))
    index_context = {"reports": []}

    for report_config in reports:

        report_root = (
            Path(destination).joinpath("reports").joinpath(report_config.subfolder)
        )

        Path(report_root).mkdir(parents=True, exist_ok=True)

        report = report_config.klass(
            data=data,
            template_name=report_config.template_name,
            root_path=report_root,
            index="index.html",
        )

        report.render()

        index_context["reports"].append(
            {
                "url": Path(report.path).relative_to(destination),
                "title": report_config.title,
            }
        )

    get_template("index.html").stream(**index_context).dump(index_path)
