import pprint


def gen_array(width, height, fill=None):
    res = list()
    for i in range(height):
        row = list()
        res.append(row)
        for j in range(width):
            row.append(fill)

    return res


# pprint.pp(gen_array(width=2,height=3,fill=0))

arr = gen_array(width=2, height=3, fill=1)


def process_row(row, func):
    acc = 0
    for item in row:
        acc += item
    return acc


pprint.pp(list(map(lambda row: process_row(row=row, func=lambda x: x**2), arr)))
