input_list = []
i = 0
n = abs(int(input('Напишите сколько элементов хотите ввести: ')))
if i <= n:
    while True:
        i += 1
        if i <= n:
            a = input(f"Введите {i}-й элемент строки: ")
            if a.isdigit():
                input_list.append(int(a))
                # print(input_list)
            else:
                input_list.append(a)
                # print(input_list)
        else:
            print_list = input_list
            # print(input_list)
            # print(print_list)
            if n % 2 == 0:
                i = 0
                while i < n:
                    element = print_list[i]
                    print_list.remove(print_list[i])
                    print_list.insert(i + 1, element)
                    i += 2
            else:
                i = 0
                while i < n - 1:
                    element = print_list[i]
                    print_list.remove(print_list[i])
                    print_list.insert(i + 1, element)
                    i += 2
            print(print_list)
            break
