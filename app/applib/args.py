import argparse

parser = argparse.ArgumentParser(description="Анализирует данные и создает отчет")

parser.add_argument("input")
parser.add_argument("sheet")

parser.add_argument("output")

parser.add_argument(
    "--force", action="store_true", help="clean destination folder if exists"
)

args = parser.parse_args()
