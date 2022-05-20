from abc import ABC, abstractmethod


class Store:

    def __init__(self, name):
        self.name = name
        self.store_tech = {}
        self.store_unit = {}

    def add_tech(self, office_tech):
        if office_tech.__class__.__name__ not in self.store_tech:
            self.store_tech[office_tech.__class__.__name__] = [office_tech]
        else:
            self.store_tech[office_tech.__class__.__name__].append(office_tech)

    def show_store(self):
        print(f'{self.name}:')
        # print(f'{self.store_tech}')
        for key, value in self.store_tech.items():
            print(f"  Наименование: {key} \n  Количество: {len(value)} шт:")
            for el in value:
                print(f'    Модель: {el.view()}')


class OfficeTech(ABC):

    def __init__(self, brand, price, pcs, serial):
        self.brand = brand
        self.price = price
        self.pcs = pcs
        self.serial = serial

    @abstractmethod
    def view(self):
        print(f"{self.brand} {self.price} {self.pcs}")

    @property
    def tech_serial(self):
        return self.serial


class Printer(OfficeTech):

    def __init__(self, brand, price, pcs, serial):
        super().__init__(brand, price, pcs, serial)
        self.serial = serial

    def view(self):
        return f"{self.brand} {self.price} {self.pcs} {self.serial}"


class Scaner(OfficeTech):

    def __init__(self, brand, price, pcs, serial):
        super().__init__(brand, price, pcs, serial)
        self.serial = serial

    def view(self):
        return f"{self.brand} {self.price} {self.pcs} {self.serial}"


class Xerox(OfficeTech):

    def __init__(self, brand, price, pcs, serial):
        super().__init__(brand, price, pcs, serial)
        self.serial = serial

    def view(self):
        return f"{self.brand} {self.price} {self.pcs} {self.serial}"


printer1 = Printer('Hewlett', 10000, 5, 'HRW-1000')
print(printer1.view())
# printer1.view_tech()
scaner1 = Scaner('Epson', 9500, 2, 'GW1-200')
print(scaner1.view())
# scaner1.view_tech()
xerox1 = Xerox('Xerox', 15500, 9, 'X01-7500')
print(xerox1.view())
# xerox1.view_tech()
# print(Printer('Epson', 12360, 2, 'GW1-105').view())
store = Store('Склад')
store.add_tech(Printer('Hewlett', 10000, 5, 'HRW-1000'))
store.add_tech(Scaner('Epson', 9500, 2, 'GW1-200'))
store.add_tech(Xerox('Xerox', 15500, 9, 'X01-7500'))
store.show_store()
store1 = Store('Офис продаж')
store1.add_tech(Printer('Hewlett', 10000, 5, 'HRW-1000'))
store1.add_tech(Printer('Epson', 12360, 2, 'GW1-105'))
store1.add_tech(Scaner('Epson', 9500, 2, 'GW1-200'))
store1.add_tech(Xerox('Xerox', 15500, 9, 'X01-7500'))
store1.add_tech(Xerox('Xerox', 19500, 1, 'X15-9000'))
store1.show_store()
store2 = Store('AХО')
store2.show_store()
