class Road:

    def __init__(self, length, width, mass=25, thickness=5):
        self._lenght = length
        self._width = width
        self.mass = mass
        self.thickness = thickness

    def calc(self):
        print(
            f"Масса асфальта необходимая для укладки на дорогу длинной {self._lenght}м и ширинной {self._width}м: "
            f"{(self._lenght * self._width * self.mass * self.thickness) / 1000} тонн")


new_road = Road(5000, 20)
new_road.calc()
