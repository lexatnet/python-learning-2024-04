import pandas as pd


data1 = pd.DataFrame(
    [
        ['k0', 'A0', 'B0'],
        ['k1', 'A1', 'B1'],
        ['k2', 'A2', 'B2'],
    ],
    columns=['key1', 'A', 'B']
)

data2 = pd.DataFrame(
    [
        ['k1','A1', 'C1', 'D1'],
        ['k2','A2', 'C2', 'D2'],
        ['k3','A3', 'C3', 'D3'],
    ],
    columns=['key2','Aa', 'C', 'D']
)

concatenated_data = pd.concat([data1, data2])

print(concatenated_data)
# print(concatenated_data.reset_index())
print(concatenated_data.reset_index().drop(columns=['index']))