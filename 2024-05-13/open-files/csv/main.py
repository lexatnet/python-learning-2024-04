# import pandas as pd

# origin_data = pd.read_csv('data.csv')

# data = origin_data.set_index('index')

# print(origin_data.head())
# print(data.head())



class Obj:
    def __init__(self):
      self.data = None

obj = Obj()
import copy
setattr(obj, "data", "a")
link = copy.copy(obj)
setattr(link, "data", "b")

print(obj.data)