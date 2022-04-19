

def my_gen():
    i = 1
    while i <= len(my_list) - 1:
        if my_list[i] > my_list[i-1]:
            new_list.append(my_list[i])
            i += 1
        else:
            i += 1
            continue
    return new_list


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
print(my_list)
# print(len(my_list))
# print(my_list[0])
print(f"Список из элементов, которые были старше предыдущих: {my_gen()}")
