from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

env = Environment(
    loader=FileSystemLoader(Path(__file__).parent.joinpath("templates")),
    autoescape=select_autoescape(),
)


def get_template(template_name):
    return env.get_template(template_name)
