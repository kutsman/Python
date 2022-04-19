# (выработка в часах*ставка в час) + премия
from sys import argv
script_name, first_param, second_param, third_param = argv
print("Имя скрипта: ", script_name)
print(f"Выработка: {first_param} Hours")
print(f"Ставка: {second_param} RUB/Hour")
print(f"Премия: {third_param} RUB")
print(f"Расчет ЗП по формуле (часы * ставка в час + премия): {int(first_param) * int(second_param) + int(third_param)} RUB")
# для запуска использовал ...>python lesson_4_task_1.py 5 1000 3000