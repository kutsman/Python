input_f = open("file_les_5_2.txt", "r")
content = input_f.readlines()
print(content)
print(f"Количество строк: {len(content)}")
i = 1
for el in content:
    print(f"Количество слов в {i}-строке: {len(el.split())}")
    i += 1
input_f.close()
