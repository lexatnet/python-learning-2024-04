from .render import get_template
from .frequency_parameters_of_process import FrequencyParametersOfProcess
from .report_1 import Report1
from pathlib import Path

reports = [
    {
        "class": FrequencyParametersOfProcess,
        "template_name": "frequency_parameters_of_process.html",
        "subfolder": "frequency_parameters_of_process",
        "title": "Частотные показатели процесса.",
    },
    {
        "class": Report1,
        "template_name": "report-1.html",
        "subfolder": "report-1",
        "title": "report 1",
    },
]


def create_reports(data, destination):
    Path(destination).mkdir(parents=True, exist_ok=True)
    index_path = str(Path(destination).joinpath("index.html"))
    index_context = {"reports": []}

    for report_config in reports:
        report_root = (
            Path(destination).joinpath("reports").joinpath(report_config["subfolder"])
        )
        Path(report_root).mkdir(parents=True, exist_ok=True)
        report = report_config["class"](
            data=data,
            template_name=report_config["template_name"],
            root_path=report_root,
            index="index.html",
        )
        report.render()
        index_context["reports"].append(
            {
                "url": Path(report.path).relative_to(destination),
                "title": report_config["title"],
            }
        )

    get_template("index.html").stream(**index_context).dump(index_path)
