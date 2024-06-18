from pathlib import Path
import shutil
import numpy as np
import pandas as pd
from applib.args import args
from applib.utils import prepare_data
from applib.reports import create_reports

from applib.logging import setup_logger
import logging

setup_logger(level=args.logging_level.to_logging_level())

logger = logging.getLogger(__name__)

logger.debug("поверка на существование директории куда будут сгенерированы отчёты")
if Path(args.output).exists():
    logger.debug("директория назначения сущетсвует")
    if args.force:
        logger.debug("удаляем сущетвующую директорию для генерации новых отчетов в то же место")
        shutil.rmtree(args.output)
    else:
        raise Exception("Директория указаная в качестве цельевой для генерации отчета уже сущетсвует.")

# Для парсинга .xlsx файлов pandas использует openpyxl. Так что необходимо его установить прописав зависимости
data = pd.read_excel(args.input, sheet_name=args.sheet)
prepared_data = prepare_data(data)

create_reports(data=prepared_data, destination=args.output)

# python app.py "/home/aromanov/tmp/Учебные_данные_февраль_апрель_обезличены.xlsx" "Лист2" "/home/aromanov/tmp/reports"
# python app.py "/home/aromanov/Downloads/Копия Учебные_данные_февраль_апрель_обезличены.xlsx" "Лист2" "/home/aromanov/tmp/reports" --log debug --force
# python .\app.py "c:\Users\user\Downloads\Учебные_данные_февраль_апрель_обезличены.xlsx" "Лист2" "c:\Users\user\Desktop\report" --log debug --force
