import matplotlib.pyplot as plt
import matplotlib

# matplotlib.use('QtAgg')
# import numpy as np

# import matplotlib as mpl

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.


fig.savefig("test.png")
# plt.show()
