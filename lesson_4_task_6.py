from itertools import count
from itertools import cycle

a = -2
print(f"Целое число с которого начинаем генерацию: {a}")
b = 13
print(f"Целое число до которого продолжаем генерацию (включительно): {b}")
my_list = []
for el in count(a):
    if el > b:
        break
    else:
        # print(el)
        my_list.append(el)
print(my_list)
list_second = []
x = int(input('Введите N - количество повторений цикла дублирования: '))
c = 1
for el in cycle(my_list):
    if c > x * (b - a + 1):
        break
    # print(el)
    c += 1
    list_second.append(el)
print(list_second)
