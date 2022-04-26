

def sum_numbers():
    for el in content:
        my_list.append(int(el))
    return sum(my_list)


out_f = open("file_les_5_5.txt", "w")
numbers = input('Введите числа через пробелы: ')
out_f.write(''.join(numbers))
out_f.close()
input_f = open("file_les_5_5.txt", "r")
my_list = []
# print(numbers)
content = input_f.read().split()
# print(content)
sum_numbers()
print(f"Cумма числел в файле: {sum(my_list)}")
input_f.close()
