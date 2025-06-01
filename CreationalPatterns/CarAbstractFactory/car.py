from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, weight, length, max_speed):
        self.weight = weight
        self.length = length
        self.max_speed = max_speed

    @abstractmethod
    def drive(self):
        print(f"Driving {self.__class__.__name__} with "
              f"(Weight: {self.weight}, Length: {self.length}, "
              f"Max Speed: {self.max_speed}km/h)")







