new_str = input('Введите любую фразу: ')
# print(new_str)
# print(len(new_str))
div_str = new_str.split()
# print(div_str)
# print(len(div_str))
i = -1
while i + 1 < len(div_str):
    i += 1
    n = div_str[i]
    if len(n) <= 10:
        print(f"{i+1}-ая строка: {n}")
    else:
        print(f"{i}-ая строка: {n[:10]}")
