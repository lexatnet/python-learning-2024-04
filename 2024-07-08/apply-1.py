import pandas as pd
import numpy as np


columns = ['name', 'birthday', 'hiered', 'fired']
# index = [1,2,3,4,5]
data = [
    ['Вася', '1986-06-06', '2021-05-05', pd.NA],
    ['Петя', '1990-01-11', '2020-03-06', pd.NA],
    ['Люда', '1992-12-01', '2022-04-07', '2022-04-07'],
    ['Иван', '1986-06-06', '2021-05-05', pd.NA],
    ['Степан', '1986-06-06', '2021-05-05', pd.NA],
]

from datetime import datetime, date


df = pd.DataFrame(data=data, columns=columns)

print(df.head)

def fun1(row, a, b):
    print(a, b)

    # birth_day = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
    # now = date.today()
    # age = now - birth_day
    # return pd.Series([0,0,0,age.days // 365.25], index=columns)
    return 1



# df['age'] = df.apply(fun1, axis='columns', result_type='expand')
res  = df.apply(fun1, axis='columns', result_type='broadcast', kwargs={'a':1,'b':2})


print(res)
