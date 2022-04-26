import json
with open("file_les_5_7.txt", "r") as f_obj:
    income = []
    company_list = []
    average_income = []
    for line in f_obj:
        # print(line)
        set_line = line.split()
        # print(set_line)
        company = set_line[0]
        company_list.append(company)
        new_gen = [int(el) for el in set_line if el.isdigit()]
        val = new_gen[0] - new_gen[1]
        if val > 0:
            average_income.append(int(val))
        income.append(val)
    # print(company_list)
    aver_prof = sum(average_income) / len(average_income)
    # print(aver_prof)
d_comp = dict(zip(company_list, income))
d_average_income = {'average_profit': aver_prof}
new_list = [d_comp, d_average_income]
print(new_list)
with open("file_les_5_7.json", "w", encoding='utf-8') as write_f:
    json.dump(new_list, write_f)
# checking up...
# with open("file_les_5_7.json") as read_f:
#     data = json.load(read_f)
#     print(data)
