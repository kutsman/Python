a = int(input('Введите число а: '))
b = int(input('Введите число b: '))


def my_dev(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Деление на ноль запрещено')
    except ValueError:
        print('Введите целое число ')


print(my_dev(a, b))
