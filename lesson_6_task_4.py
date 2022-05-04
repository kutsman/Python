class Car:
    speed = 65
    color = 'red'
    name = 'Dodge'
    is_police = True
    direction = 'left'

    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        if self.is_police:
            print(f"{self.name}(police car) поехал")
        else:
            print(f"{self.name} поехал")

    def stop(self):
        print(f"Машина остановилась")

    def turn(self):
        if self.direction == 'right':
            print(f"Машина повернула направо")
        else:
            print(f"Машина повернула налево")

    def show_speed(self):
        print(f"Cкорость: {self.speed} км\ч")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость: {self.speed}км\ч. Alarm! Вы превысили скорость")
        else:
            print(f"Cкорость: {self.speed} км\ч")

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость: {self.speed}км\ч. Alarm! Вы превысили скорость")
        else:
            print(f"Cкорость: {self.speed} км\ч")

class SportCar(Car):
    pass


class PoliceCar(Car):
    pass

car_1 = TownCar(61, 'Blue', 'BMW', None, 'left')
car_1.go()
car_1.show_speed()
car_1.turn()
car_1.stop()
car_2 = WorkCar(45, 'Black', 'GMC', None, 'right')
car_2.go()
car_2.show_speed()
car_2.turn()
car_2.stop()
car_3 = SportCar(120, 'Black', 'Ferrari', None, 'left')
car_3.go()
car_3.show_speed()
car_3.turn()
car_3.stop()
car_4 = Car(100, 'White', 'Ford', True, 'left')
car_4.go()
car_4.show_speed()
car_4.turn()
car_4.stop()
