import numpy as np
import pandas as pd


def prepare_data(data):
    # Желательно удалить неиспользуемые столбцы и строки из датафрейма
    data1 = data.drop(index=[0, 1]).reset_index()

    # Так же переназвать колонки

    def my_mapper(column):
        new_name = data1.at[0, column]
        if pd.notna(new_name):
            return new_name
        return column

    data2 = data1.rename(mapper=my_mapper, axis="columns")

    # теперь можем удалить неиспользованую строку

    data2 = data2.drop(index=[0]).reset_index()

    # Найдём неиспользуемые колонки

    unnamed_columns = list(
        filter(lambda x: str(x).startswith("Unnamed"), data2.columns)
    )

    # проверим что неиспользуемые колонки пустые

    for col in unnamed_columns:
        data2[col].unique()

    # Анализ колонки на содержание непустых значений возвращает данные если они есть иначе пустой DF
    # data2[data2[col].notnull()]

    for col in unnamed_columns:
        if data2[data2[col].notnull()].empty:
            data2 = data2.drop(columns=[col])

    # print(data2.head())

    return data2
