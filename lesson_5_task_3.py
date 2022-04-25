input_f = open("file_les_5_3.txt", "r")
content = input_f.readlines()
print(content)
# print(f"Количество строк: {len(content)}")
income = []
for el in content:
    money = el.split()[1]
    if float(money) < 20000:
        income.append(float(money))
        print(f"Сотрудники с окладом менее 20000 руб.: {el.split()[0]}")
    else:
        income.append(float(money))
middle_income = sum(income) / len(income)
print(f"Средний доход сотрудников: {middle_income:.2f} руб.")
input_f.close()
