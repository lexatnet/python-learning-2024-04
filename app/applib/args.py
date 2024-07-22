import argparse
from .logging_level import LoggingLevel

parser = argparse.ArgumentParser(description="Анализирует данные и создает отчет")

parser.add_argument("input", help=".xlsx файл с исходными данными")
parser.add_argument("sheet", help="лист содержащий данные в файле")
parser.add_argument(
    "output", help="директория назначения в которую будут сгенерированы отчеты"
)

parser.add_argument(
    "--force",
    action="store_true",
    help="удалить всё содержимое директории назначения если она существует",
)

parser.add_argument(
    "--log",
    dest="logging_level",
    default="error",
    choices=[i.value for i in LoggingLevel],
    type=LoggingLevel,
    help=(
        "уровень логирования,"
        " error - выводится только информация об ошибках,"
        " info - выводится вспомогательная информация информационного характера,"
        " debug - выводится наиболее подробная информация о ходе работы приложения"
    ),
)


args = parser.parse_args()
