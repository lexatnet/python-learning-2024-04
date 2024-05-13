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
        ['k1', 'C1', 'D1'],
        ['k2', 'C2', 'D2'],
        ['k3', 'C3', 'D3'],
    ],
    columns=['key2', 'C', 'D']
)

merged_data = data1.merge(data2, left_on='key1', right_on='key2', how='outer')

print(merged_data)