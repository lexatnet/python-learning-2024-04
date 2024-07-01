from functools import cache


@cache
def f1(x, y):
    print('call func1()')
    return f2(x)+y


def f2(a):
    print('call func2()')
    return a**2

v1 = f1(1, 2)
print('v1', v1)
v2 = f1(2, 2)
print('v2', v2)
v3 = f1(1, 2)
print('v3', v3)