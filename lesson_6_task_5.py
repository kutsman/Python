class Stationery:

    def __init__(self, title='...'):
        self. title = title

    def draw(self):
        print(f"Запуск отрисовки c {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отприсовки ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отприсовки карандашом {self.title}")


class Marker(Stationery):
    def draw(self):
        print(f"Запуск отприсовки маркером {self.title}")


first_st = Stationery()
first_st.draw()
second_st = Pen('Big')
second_st.draw()
third_st = Pencil('Stabilo')
third_st.draw()
fourth_st = Marker('Colorfil')
fourth_st.draw()
