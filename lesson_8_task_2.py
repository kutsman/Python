class DivideZero(Exception):
    pass


def div_calc():
    c = 'y'
    while c == 'y':
        a = int(input('Введите значение a: '))
        # print(f"Значение а = {a}")
        b = int(input('Введите значение b: '))
        # print(f"Значение а = {b}")
        if b != 0:
            c = a / b
            print(f"a/b = {c:.2f}")
            c = input('Введите y(yes) чтобы продолжить или q(quit), чтобы выйти: ')
        else:
            print("Деление на 0 запрещено, введите значение b больше или меньше нуля!")
            c = input('Введите y (yes) чтобы продолжить или q(quit), чтобы выйти: ')
    else:
        print("Вы вышли, спасибо за использование!")


div_calc()
