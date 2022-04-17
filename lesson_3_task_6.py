

def int_func():
    i = 0
    while i <= len(new_str) - 1:
        if new_str[i].islower():
            input_list.append(new_str[i].title())
        else:
            input_list.append(new_str[i].lower().title())
        i += 1
    else:
        return " ".join(input_list)


input_list = []
str_1 = input('Введите строку из латинских слов или набора букв: ')
# str_1 = 'Hello BROTHER EvERYday CoolER'
# str_1 = 'hello BROTHER everyday cooler'
new_str = str_1.split()
print(int_func())
