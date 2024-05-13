import pandas as pd

data_source = pd.read_excel('groupby-data.xlsx')
print(data_source)

print(data_source.groupby(["a", "b"]).count())