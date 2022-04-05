income = input("Введите выручку фирмы: ")
# print(f"Выручка фирмы составила: {income} рублей")
costs = input("Введите расходы фирмы: ")
# print(f"Расходы фирмы составили: {costs} рублей")
if int(income) > int(costs):
    print(f"Фирма отработа с прибылью, которая составила: {(int(income) - int(costs))} рублей")
    result = (int(income) - int(costs)) / int(income) * 100
    print(f"Рентабельность фирмы составила: {result:.2f} %")
persons = int(input("Введите количество сотрудников: "))
if persons > 0:
    income_per_person = (int(income) - int(costs)) / persons
    print(f"Прибыль фирмы на одного сотрудника составила: {income_per_person:.2f} рублей")
else:
    print(f"Фирма отработала с убытком: {abs(int(income) - int(costs))} рублей")
