class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def list(cls, date):
        date_list = []
        for el in date.split('-'):
            if el.isdigit():
                date_list.append(int(el))
            else:
                print("Вы нарушили формат ввода дд-мм-гг")
                break
        return date_list

    @staticmethod
    def check_date(date):
        day_month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        while Data.list(date)[2] <= 2022:
            if Data.list(date)[1] in list(day_month_dict.keys()):
                if Data.list(date)[0] <= day_month_dict.get(Data.list(date)[1]):
                    return f"Проверка: Все впорядке! В {Data.list(date)[1]}-м месяце дней может быть не более " \
                           f"{day_month_dict.get(Data.list(date)[1])}"
                else:
                    return f"Проверка: Ошибка! Вы ввели дней больше чем в {Data.list(date)[1]}-м месяце"
            else:
                return f"Проверка: Ошибка! Месяцев в году только 12!"
        else:
            return f"Упс, ты кажется забрался в будущее"


date1 = Data('11-05-2022')
date2 = Data('09-10-1985')
# print(date1.list('fdf-05-2022'))
print(date1.list('11-05-2022'))
print(date2.list('09-10-1985'))
print(date1.list('29-02-2022'), date1.check_date('29-02-2022'))
# print(date1.check_date('29-02-2022'))
print(date1.list('30-13-2022'), date1.check_date('30-13-2022'))
print(date1.list('29-02-2024'), date1.check_date('29-02-2024'))
# print(date1.check_date('29-02-2022'))
print(date1.list('30-12-1000'), date1.check_date('30-12-1000'))
