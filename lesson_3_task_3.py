a = 5
b = 8
c = 10
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


def my_func(a, b, c):
    if a > b > c:
        return a + b
    if b > a > c:
        return a + b
    if c > a > b:
        return c + a
    if c > b > a:
        return c + b


print(f"Cумма двух больших аргументов равна: {my_func(a, b, c)}")
