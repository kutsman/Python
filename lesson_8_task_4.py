class Store:
    pass


class OfficeTech:

    def __init__(self, brand, price, pcs):
        self.brand = brand
        self.price = price
        self.pcs = pcs

    def view_tech(self):
        print(f"{self.brand} {self.price} {self.pcs}")


class Printer(OfficeTech):

    def __init__(self, brand, price, pcs, serial):
        super().__init__(brand, price, pcs)
        self.serial = serial

    def view(self):
        return f"{self.brand} {self.price} {self.pcs} {self.serial}"


class Scaner(OfficeTech):

    def __init__(self, brand, price, pcs, serial):
        super().__init__(brand, price, pcs)
        self.serial = serial

    def view(self):
        return f"{self.brand} {self.price} {self.pcs} {self.serial}"


class Xerox(OfficeTech):

    def __init__(self, brand, price, pcs, serial):
        super().__init__(brand, price, pcs)
        self.serial = serial

    def view(self):
        return f"{self.brand} {self.price} {self.pcs} {self.serial}"


printer1 = Printer('Hewlett', 10000, 5, 'HRW-1000')
print(printer1.view())
printer1.view_tech()
scaner1 = Scaner('Epson', 9500, 2, 'GW1-200')
print(scaner1.view())
# scaner1.view_tech()
xerox1 = Xerox('Xerox', 15500, 9, 'X01-7500')
print(xerox1.view())
# xerox1.view_tech()
