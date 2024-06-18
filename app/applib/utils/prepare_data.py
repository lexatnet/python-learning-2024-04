import numpy as np
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def prepare_data(data):
    # Желательно удалить неиспользуемые столбцы и строки из датафрейма
    data1 = data.drop(index=[0, 1]).reset_index()

    # Так же переназвать колонки

    def my_mapper(column):
        logger.debug(f"переименование колонки {column}")
        backup_columls = ['index']
        if column in backup_columls:
            new_name = f'src_{column}'
            logger.debug(f"сохраняем  {column} в {new_name}")
            return new_name
        
        new_name = data1.at[0, column]
        if pd.notna(new_name) and str(column).startswith("Unnamed"):
            logger.debug(f"найдено имя {new_name}")
            return new_name
        return column

    data2 = data1.rename(mapper=my_mapper, axis="columns")

    logger.debug(f"переименованные колонки:\n{data2.head()}")

    # теперь можем удалить неиспользованую строку
    data2 = data2.drop(index=[0]).reset_index()

    logger.debug(f"Сбошенный индекс:\n{data2.head()}")

    # Найдём неиспользуемые колонки
    unnamed_columns = list(
        filter(lambda x: str(x).startswith("Unnamed"), data2.columns)
    )

    logger.debug(f"Неименованные колонки: {unnamed_columns}")

    # проверим что неиспользуемые колонки пустые
    # Анализ колонки на содержание непустых значений возвращает данные если они есть иначе пустой DF
    # data2[data2[col].notnull()]

    for col in unnamed_columns:
        if data2[data2[col].notnull()].empty:
            logger.debug(f"Колонка {col} пустая, исключаем из данных")
            data2 = data2.drop(columns=[col])
        else:
            logger.warning(f"Колонка {col} непустая, но неименована. Возможно некорректные исходные данные.")

    logger.debug(f"Подготовленые исходные данные:\n{data2.head()}")

    return data2
