import pandas as pd

df = pd.DataFrame(
    [[0, 2, 3], [0, 4, 1], [10, 20, 30]], index=[4, 5, 6], columns=["A", "B", "C"]
)

for col in df:
    for row in df[col].index:
        val = str(df[col][row])
        if "0" in val:
            df.at[row, col] = 1


print(df)


# import matplotlib.pyplot as plt
# import matplotlib

# # matplotlib.use('QtAgg')
# # import numpy as np

# # import matplotlib as mpl

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.


# fig.savefig("test.png")
# # plt.show()
