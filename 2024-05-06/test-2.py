x = lambda m1, m2, r, g : ((m1 * m2)/r**r) * g

def low_1(m1, m2, r, g): 
    return ((m1 * m2)/r**r) * g


map(arr, low_1)