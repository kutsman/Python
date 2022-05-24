class NumList(Exception):
    pass


def numeric():
    new_list = []
    c = 'y'
    while c != 'q':
        a = input('Введите элемент списка (число): ')
        # print(a.split('-'))
        # print(len(a.split('-')))
        if len(a.split('-')) == 1:
            if a.isdigit():
                new_list.append(int(a))
                print(new_list)
                c = input('Введите enter чтобы продолжить или q(quit), чтобы выйти: ')
            else:
                print("Вы ввели не число, пожалуйста введите число")
        else:
            if len(a.split('-')) == 2:
                if a.split('-')[0] == '':
                    new_list.append(-int(a.split('-')[1]))
                    print(new_list)
                    c = input('Введите enter чтобы продолжить или q(quit), чтобы выйти: ')
                else:
                    print("Вы ввели не число, пожалуйста введите число")
            else:
                print("Вы ввели не число, пожалуйста введите число")
    else:
        print(f"Вы вышли, спасибо за использование!\nВаш итоговый список чисел: {new_list}")


numeric()
