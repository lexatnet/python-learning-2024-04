x_offset = 0
y_offset = 0
x_step = 0
y_step = 0

def create_width_legend(width, start, stop):
    pass

def create_height_legend():
    pass

def func(x):
    return x - 2

def gen_plane(width, height, fill = ' '):
    plane = []
    for i in range(height):
        row = []
        plane.append(row)
        for j in range(width):
            row.append(fill)




def graphic(
        width, 
        height,
        values,
        x_offset,
        y_offset,
        x_step = 1,
        y_step = 1,
    ):

    vals = filter(lambda x, y: x < width and y < height ,values)
    plane = gen_plane(width, height, fill = ' ')

    x_delta = width / x_step
    y_delta = height / y_step


    for x, y in vals:
        
