input_f = open("file_les_5_4.txt", "r")
out_f = open("file_les_5_4_1.txt", "w")
content = input_f.readlines()
print(content)
lang_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
lang_list_replace = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь']
new_list = []
for el in content:
    new_el = el.split()
    if new_el[0] in lang_list:
        index_pos = lang_list.index(new_el[0])
        new_el.remove(new_el[0])
        new_el.insert(0, lang_list_replace[index_pos])
        new_str = ' '.join(new_el)
        new_list.append(new_str)
print(new_list)
out_f.writelines('\n'.join(new_list))
input_f.close()
out_f.close()
