out_f = open("file_les_5_1.txt", "w", encoding='utf-8')
name = input('Введите свое Имя: ')
city = input('Введите город, в котором живете:')
email = input('Введите свой e-mail: ')
phone = input('Введите свой номер телефона: ')
my_info = [name, city, email, phone]
out_f.writelines('\n'.join(my_info))
out_f.close()
