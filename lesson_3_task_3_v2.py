

def my_func(a, b, c):
    if a > b > c:
        return a + b
    if a > b and c > b:
        return a + c
    if b > a > c:
        return a + b
    if b > a and a < c:
        return b + c
    if c > a > b:
        return c + a
    if c > b > a:
        return c + b


a = 1978
b = 1
c = 2
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"Cумма двух больших аргументов равна: {my_func(a, b, c)}")
