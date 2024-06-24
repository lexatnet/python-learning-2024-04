from pathlib import Path
import shutil
import numpy as np
import pandas as pd
from applib.args import args
from applib.utils import prepare_data
from applib.utils.time_meter import time_meter_context_manager, time_meter_decorator

from applib.reports import create_reports
from datetime import datetime

from applib.logging import setup_logger, logging_section
import logging

setup_logger(level=args.logging_level.to_logging_level())

logger = logging.getLogger(__name__)

logger.debug("поверка на существование директории куда будут сгенерированы отчёты")
if Path(args.output).exists():
    logger.debug("директория назначения существует")
    if args.force:
        logger.debug(
            "удаляем существующую директорию для генерации новых отчетов в то же место"
        )
        shutil.rmtree(args.output)
    else:
        raise Exception(
            "Директория указанная в качестве целевой для генерации отчета уже существует."
        )

# Для парсинга .xlsx файлов pandas использует openpyxl. Так что необходимо его установить прописав зависимости

logger.debug("Чтение файла данных...")

from datetime import datetime

start_time = datetime.now()
data = pd.read_excel(args.input, sheet_name=args.sheet)
end_time = datetime.now()
logger.debug(f"заняло {(end_time - start_time).total_seconds()}сек.")

logger.debug("Чтение файла данных завершено")

# label = "Чтение файла данных"
# with (
#     logging_section(logger, label=label) as ls,
#     time_meter_context_manager(logger, label=label) as tmc,
# ):
#     data = pd.read_excel(args.input, sheet_name=args.sheet)

logger.debug("Подготовка данных...")
prepared_data = time_meter_decorator(logger)(prepare_data)(data)

create_reports(data=prepared_data, destination=args.output)

# python app.py "/home/aromanov/tmp/Учебные_данные_февраль_апрель_обезличены.xlsx" "Лист2" "/home/aromanov/tmp/reports"
# python app.py "/home/aromanov/Downloads/Копия Учебные_данные_февраль_апрель_обезличены.xlsx" "Лист2" "/home/aromanov/tmp/reports" --log debug --force
# python .\app.py "c:\Users\user\Downloads\Учебные_данные_февраль_апрель_обезличены.xlsx" "Лист2" "c:\Users\user\Desktop\report" --log debug --force
