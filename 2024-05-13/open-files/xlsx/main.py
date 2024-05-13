import pandas as pd

origin_data = pd.read_excel('data.xlsx')

data = origin_data.set_index('index')

print(data.head())