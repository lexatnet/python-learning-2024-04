import pandas as pd


data = pd.DataFrame(
    [
        ["col(1, 0)", "col(2,0)", "col(3,0)"],
        ["col(1, 1)", "col(2,1)", "col(3,1)"],
        ["col(1, 2)", "col(2,2)", "col(3,2)"],
    ],
    columns=["col1", "col2", "col3"],
)
print(data.head())

data.to_csv("data.csv")
