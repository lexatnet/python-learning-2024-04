import pandas as pd

origin_data = pd.read_csv('data.csv')

data = origin_data.set_index('index')

print(data.head())