from abc import ABC, abstractmethod


class Cloth(ABC):
    summary_material = 0

    @abstractmethod
    def calc_material(self):
        pass


class Coat(Cloth):

    def __init__(self, size):
        self.size = size
        Cloth.summary_material += self.calc_material

    def __str__(self):
        return f"На пальто с размером {self.size} ушло {self.calc_material:.2f}м"

    @property
    def calc_material(self):
        return self.size / 6.5 + 0.5


class Suit(Cloth):

    def __init__(self, height):
        self.height = height
        Cloth.summary_material += self.calc_material

    def __str__(self):
        return f"На костюм ростовки {self.height} ушло {self.calc_material:.2f}м"

    @property
    def calc_material(self):
        return 2 * self.height + 0.3


coat_1 = Coat(32)
print(coat_1)
coat_2 = Coat(24)
print(coat_2)
suit_1 = Suit(2)
print(suit_1)
suit_2 = Suit(3)
print(suit_2)
print(f"Всего на все пальто и костюмы ушло ткани: {Cloth.summary_material: .2f}м")
