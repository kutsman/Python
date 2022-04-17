

def digit_sum():
    i = 0
    while i <= len(new_str) - 1:
        if new_str[i].isdigit():
            input_list.append(int(new_str[i]))
            i += 1
        else:
            input_list_letter.append(new_str[i])
            # print(input_list)
            # return sum(input_list)
            # print(len(input_list))
            return sum(input_list)
        continue
    else:
        return sum(input_list)


input_list = []
input_list_letter = []
str_1 = input('Введите список цифр через пробелы (если в списке будут буквы, '
              'функция возьмет для сумирование цифры до этой буквы и ОСТАНОВИТСЯ!): ')
new_str = str_1.split()
# print(new_str)
# print(len(new_str))
# print(digit_sum())
sum_digit = 0
g = 0   
while True:
    sum_digit = digit_sum()
    # print(f"Cумма всех элементов равна: {sum_digit}")
    g = g + len(new_str)      # добавляю новые цифры в список и считаю длину итогового
    if len(input_list) == g:  # делаю сверку, если попадается буква(-ы), элементов будет меньше на один
        print(f"Cумма всех элементов равна: {sum_digit}")
        new_str = input('Введите список цифр через пробелы, он добавится к предыдущей сумме: ').split()
    else:
        print(f"Cумма всех элементов с учетом цифр до букв(-ы) '{input_list_letter[0]}' равно: {sum_digit}")
        break
