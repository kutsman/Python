with open("file_les_5_6.txt", "r", encoding='utf-8') as f_obj:
    hours = []
    keys = []
    for line in f_obj:
        line = line.replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace('—', '0')
        # print(line)
        set_line = line.split()
        new_study = set_line[0]
        keys.append(new_study.replace(':', ''))
        for el in set_line:
            new_gen = [int(el) for el in set_line if el.isdigit()]
            val = sum(new_gen)
        # print(sum(new_gen))
        hours.append(val)
# print(f"Список сумм часов по всем предметам: {hours}")
# print(f"Список сумм часов по всем предметам: {keys}")
d = dict(zip(keys, hours))
print(f"Словарь: {d}")
