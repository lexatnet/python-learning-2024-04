
table = [
    [1,2,3],
    [2,2,3],
    [3,4,3],
    [4,2,3],
]

table2 = [
    [1,2,3],
    [2,2,3],
    [3,2,3],
    [4,2,3],
]

def is_exists(table):
    return any((row[1] == 4 for row in table))

print(is_exists(table=table))
print(is_exists(table=table2))