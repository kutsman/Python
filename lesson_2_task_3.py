month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
month_number = abs(int(input('Введите порядковый номер месяца (от 1 до 12): ')))
while True:
    if month_number in month:
        if month_number in winter:
            print('Время года - зима')
            break
        if month_number in spring:
            print('Время года - весна')
            break
        if month_number in summer:
            print('Время года - лето')
            break
        if month_number in autumn:
            print('Время года - осень')
            break
    else:
        print('Увы, в году всего 12 месяцев, проверьте, чтобы введенный месяц имел значение от 1 до 12!')
        month_number = abs(int(input('Введите порядковый номер месяца (от 1 до 12): ')))
