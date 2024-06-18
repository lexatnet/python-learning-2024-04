x = "external"


def f():
    count = 0

    def b():
        nonlocal count
        x = 1
        count += 1
        return count

    def a():
        return count

    return b, a


b, a = f()

print(a())
b()
b()
b()

print(a())

b()
b()

print(a())
# c, d = f()
