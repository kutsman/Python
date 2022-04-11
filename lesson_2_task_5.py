my_list = [7, 5, 3, 3, 2, 0, -5]
print(my_list)
str_len = len(my_list)
new_element = int(input('Введите новое целое число: '))
if new_element in my_list:
    index = my_list.index(new_element)
    number_of_similar_element = my_list.count(new_element)
    my_list.insert(index + number_of_similar_element, new_element)
    print(my_list)
else:
    if new_element > my_list[0]:
        my_list.insert(0, new_element)
        print(my_list)
    if new_element < my_list[str_len-1]:
        my_list.append(new_element)
        print(my_list)
if new_element < my_list[0] and new_element > my_list[str_len - 1]:
    i = 0
    while True:
        i += 1
        if new_element < my_list[i-1] and new_element > my_list[i]:
            my_list.insert(i, new_element)
            print(my_list)
            break







