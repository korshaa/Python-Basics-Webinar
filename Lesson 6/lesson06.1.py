import time


class TrafficLight:
    def __init__(self):
        self.__color_stop = "Red"
        self.__color_ready = "Yellow"
        self.__color_go = "Green"

    def running(self):
        while True:
            print(f'\r{self.__color_stop}', end="", flush=True)
            time.sleep(7)
            print(f'\r{self.__color_ready}', end="", flush=True)
            time.sleep(2)
            print(f'\r{self.__color_go}', end="", flush=True)
            time.sleep(10)


tl_light = TrafficLight()
tl_light.running()
