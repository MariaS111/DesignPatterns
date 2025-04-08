from car import Car
from enums import VehicleClass, VehicleWheelDrive

class Vehicle(Car):
    def __init__(self, weight, length, max_speed, wheel_drive: VehicleWheelDrive, vehicle_class: VehicleClass, color):
        super().__init__(weight, length, max_speed)
        self.wheel_drive = wheel_drive
        self.vehicle_class = vehicle_class
        self.color = color

    def drive(self):
        print(f"Driving {self.__class__.__name__} with "
              f"Color: {self.color}, Class: {self.vehicle_class.value}, "
              f"Wheel Drive: {self.wheel_drive.value}, Max Speed: {self.max_speed}km/h")


# Vehicles
class Tesla(Vehicle):
    def __init__(self):
        super().__init__(weight=2000, length=4.7, max_speed=250,
                         wheel_drive=VehicleWheelDrive.FR,
                         vehicle_class=VehicleClass.SEDAN,
                         color="red")


class Audi(Vehicle):
    def __init__(self):
        super().__init__(weight=1800, length=4.6, max_speed=240,
                         wheel_drive=VehicleWheelDrive.BACK,
                         vehicle_class=VehicleClass.COUPE,
                         color="black")


class Honda(Vehicle):
    def __init__(self):
        super().__init__(weight=1700, length=4.4, max_speed=220,
                         wheel_drive=VehicleWheelDrive.FR,
                         vehicle_class=VehicleClass.HATCHBACK,
                         color="white")