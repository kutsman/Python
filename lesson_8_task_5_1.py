from abc import ABC, abstractmethod


class Store:

    def __init__(self, name):
        self.name = name
        self.store_tech = {}
        self.store_unit = {}

    def add_tech(self, office_tech):
        if office_tech.__class__.__name__ is self.store_tech:
            self.store_tech[office_tech.__class__.__name__].append(office_tech)
            # office_tech.list_made()
        else:
            self.store_tech[office_tech.__class__.__name__] = [office_tech]
            # self.store_tech[office_tech.__class__.__name__].append(office_tech.list_made())
            # print(f'{office_tech.list_made()}')

    def show_store(self):
        print(f'{self.name}:')
        # print(f'{self.store_tech}')
        for key, value in self.store_tech.items():
            print(f"  Наименование: {key} \n  Количество: {len(value)} шт.")
            for el in value:
                print(f'    Модель: {el.view()}')

    def move_tech(self, unit, office_tech):
        if office_tech.__class__.__name__ not in self.store_tech:
            print(f"{office_tech.__class__.__name__} нет в {self.name}")
        new_list = list(
            filter(lambda i: i.serial == office_tech.serial, self.store_tech[office_tech.__class__.__name__]))
        if len(new_list) == 0:
            print(f"Устройство с таким серийным номером {office_tech.serial} нет в {self.name}")
        self.store_tech[office_tech.__class__.__name__].remove(new_list[0])
        if unit is self.store_unit:
            self.store_unit[unit].append(new_list[0])
        else:
            self.store_unit[unit] = [new_list[0]]

    def unit_items(self):
        for key, value in self.store_unit.items():
            print(f"{key}:  \n  Получил: {len(value)} шт.")
            for el in value:
                print(f'    Модель: {el.view()}')


class OfficeTech(ABC):

    def __init__(self, brand, price, serial):
        self.brand = brand
        self.price = price
        self.serial = serial
        self.new_list = []

    @abstractmethod
    def view(self):
        print(f"{self.brand} {self.price}")

    @property
    def tech_serial(self):
        return self.serial

    # def list_made(self):
    #     self.new_list.append(self.brand)
    #     self.new_list.append(self.price)
    #     self.new_list.append(self.serial)
    #     return self.new_list


class Printer(OfficeTech):
    def view(self):
        return f"{self.brand} {self.price} {self.serial}"


class Scaner(OfficeTech):
    def view(self):
        return f"{self.brand} {self.price} {self.serial}"


class Xerox(OfficeTech):
    def view(self):
        return f"{self.brand} {self.price} {self.serial}"


store = Store('Склад')
store.add_tech(Printer('Hewlett', 10000, 'HRW-1000'))
store.add_tech(Scaner('Epson', 9500, 'GW1-200'))
store.add_tech(Xerox('Xerox', 19500, 'X15-9000'))
store.show_store()
store1 = Store('Офис продаж')
store1.add_tech(Printer('Hewlett', 10000, 'HRW-1000'))
store1.add_tech(Printer('Epson', 12360, 'GW1-105'))
store1.add_tech(Scaner('Epson', 9500, 'GW1-200'))
store1.show_store()
store.move_tech('АХО', Xerox('Xerox', 19500, 'X15-9000'))
store.unit_items()
store.show_store()
