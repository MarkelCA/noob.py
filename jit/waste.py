def f(x, y):
    return x + y

a = 0
for _ in range(10000000):
    a += f(2,3)

