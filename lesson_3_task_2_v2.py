

def show_data(name, surname, birth_date, city, email, phone):
    return f"Имя: {name} Фамиля: {surname} Дата рождения: {birth_date} Город: {city} E-mail: {email} Телефон: {phone}"


# print(show_data(name , surname, birth_date, city, email, phone))
# задал с помощью именных
print(show_data(name=input('Введите свое имя: '), surname=input('Введите свою фамилию: '),
                birth_date=input('Введите дату рождения: '), city=input('Введите город проживания: '),
                email=input('Введите свой e-mail: '), phone=input('Введите свой телефон: ')))
