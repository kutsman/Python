import time


class TrafficLight:
    colors = [[['red'], [7, 31]], [['yellow'], [2, 33]], [['green'], [5, 32]]]

    def __init__(self, color=None):
        if color is None:
            color = ['red', 'yellow', 'green']
        self.__color = color

    def running(self):
        while True:
            for el in self.colors:
                print(f"\033[{el[1][1]}m{el[0][0]} - переключится через {el[1][0]} сек...")
                time.sleep(int(el[1][0]))


trafficlight = TrafficLight()
trafficlight.running()
