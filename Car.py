from enum import Enum
from abc import ABC, abstractmethod


class VehicleClass(Enum):
    HATCHBACK = "hatchback"
    SEDAN = "sedan"
    COUPE = "coupe"


class VehicleWheelDrive(Enum):
    FR = "front"
    BACK = "back"


class Car:
    def __init__(self, weight, length, max_speed):
        self.weight = weight
        self.length = length
        self.max_speed = max_speed

    def drive(self):
        print(f"Driving a generic car at {self.max_speed} km/h.")


class Vehicle(Car):
    def __init__(self, weight, length, max_speed, wheel_drive: VehicleWheelDrive, vehicle_class: VehicleClass, color):
        super().__init__(weight, length, max_speed)
        self.wheel_drive = wheel_drive
        self.vehicle_class = vehicle_class
        self.color = color

    def drive(self):
        print(f"Driving a {self.color} {self.vehicle_class.value} vehicle with {self.wheel_drive.value} drive.")


class Cargo(Car):
    def __init__(self, weight, length, max_speed, tonnage, tank_volume, axles_amount):
        super().__init__(weight, length, max_speed)
        self.tonnage = tonnage
        self.tank_volume = tank_volume
        self.axles_amount = axles_amount

    def drive(self):
        print(f"Driving a cargo truck with {self.tonnage}t capacity and {self.axles_amount} axles.")


class Tank(Car):
    def __init__(self, weight, length, max_speed, projectile_caliber, shots_per_minute, crew_size):
        super().__init__(weight, length, max_speed)
        self.projectile_caliber = projectile_caliber
        self.shots_per_minute = shots_per_minute
        self.crew_size = crew_size

    def drive(self):
        print(f"Driving a tank with {self.projectile_caliber} caliber and crew of {self.crew_size}.")


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


# Cargo
class Volvo(Cargo):
    def __init__(self):
        super().__init__(weight=8000, length=7.5, max_speed=120,
                         tonnage=15, tank_volume=500, axles_amount=4)


class Man(Cargo):
    def __init__(self):
        super().__init__(weight=7700, length=7.2, max_speed=115,
                         tonnage=16, tank_volume=480, axles_amount=5)


class Scania(Cargo):
    def __init__(self):
        super().__init__(weight=8200, length=7.8, max_speed=125,
                         tonnage=18, tank_volume=500, axles_amount=5)


# Tanks
class Tiger(Tank):
    def __init__(self):
        super().__init__(weight=45000, length=6.1, max_speed=45,
                         projectile_caliber=88, shots_per_minute=9, crew_size=3)


class Abrams(Tank):
    def __init__(self):
        super().__init__(weight=50000, length=7.2, max_speed=50,
                         projectile_caliber=120, shots_per_minute=8, crew_size=4)


class Merkava(Tank):
    def __init__(self):
        super().__init__(weight=55000, length=7.5, max_speed=60,
                         projectile_caliber=120, shots_per_minute=9, crew_size=4)


class AbstractCarFactory(ABC):
    @abstractmethod
    def create_car(self, brand: str) -> Car:
        pass


class VehicleFactory(AbstractCarFactory):
    def create_car(self, brand: str):
        if brand == "Tesla":
            return Tesla()
        elif brand == "Audi":
            return Audi()
        elif brand == "Honda":
            return Honda()
        raise ValueError("Unknown vehicle brand")


class CargoFactory(AbstractCarFactory):
    def create_car(self, brand: str):
        if brand == "Scania":
            return Scania()
        elif brand == "Volvo":
            return Volvo()
        elif brand == "Man":
            return Man()
        raise ValueError("Unknown cargo brand")


class TankFactory(AbstractCarFactory):
    def create_car(self, brand: str):
        if brand == "Tiger":
            return Tiger()
        elif brand == "Abrams":
            return Abrams()
        elif brand == "Merkava":
            return Merkava()
        raise ValueError("Unknown tank brand")


def client_code(factory: AbstractCarFactory, brand: str):
    car = factory.create_car(brand)
    car.drive()


if __name__ == "__main__":
    client_code(VehicleFactory(), "Tesla")
    client_code(CargoFactory(), "Volvo")
    client_code(TankFactory(), "Merkava")
