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
        print(f"Driving a {self.__class__.__name__} "
              f"(Weight: {self.weight}, Length: {self.length}, "
              f"Max Speed: {self.max_speed}km/h)")


class Vehicle(Car):
    def __init__(self, weight, length, max_speed, wheel_drive: VehicleWheelDrive, vehicle_class: VehicleClass, color):
        super().__init__(weight, length, max_speed)
        self.wheel_drive = wheel_drive
        self.vehicle_class = vehicle_class
        self.color = color

    def drive(self):
        print(f"Driving a {self.__class__.__name__} "
              f"(Color: {self.color}, Class: {self.vehicle_class.value}, "
              f"Wheel Drive: {self.wheel_drive.value}, Max Speed: {self.max_speed}km/h)")


class Cargo(Car):
    def __init__(self, weight, length, max_speed, tonnage, tank_volume, axles_amount):
        super().__init__(weight, length, max_speed)
        self.tonnage = tonnage
        self.tank_volume = tank_volume
        self.axles_amount = axles_amount

    def drive(self):
        print(f"Driving a {self.__class__.__name__} "
              f"(Tonnage: {self.tonnage}t, Tank Volume: {self.tank_volume}L, "
              f"Axles: {self.axles_amount}, Max Speed: {self.max_speed}km/h)")


class Tank(Car):
    def __init__(self, weight, length, max_speed, projectile_caliber, shots_per_minute, crew_size):
        super().__init__(weight, length, max_speed)
        self.projectile_caliber = projectile_caliber
        self.shots_per_minute = shots_per_minute
        self.crew_size = crew_size

    def drive(self):
        print(f"Driving a {self.__class__.__name__} "
              f"(Caliber: {self.projectile_caliber}mm, RPM: {self.shots_per_minute}, "
              f"Crew: {self.crew_size}, Max Speed: {self.max_speed}km/h)")


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
    def create_vehicle(self) -> Vehicle:
        pass

    @abstractmethod
    def create_cargo(self) -> Cargo:
        pass

    @abstractmethod
    def create_tank(self) -> Tank:
        pass


class DefaultCarFactory(AbstractCarFactory):
    def create_vehicle(self):
        return Audi()  # Honda, Tesla

    def create_cargo(self):
        return Volvo()  # Man, Scania

    def create_tank(self):
        return Tiger()  # Abrams, Merkava


class FirstClientCarFactory(AbstractCarFactory):
    def create_vehicle(self):
        return Honda()  # Audi, Tesla

    def create_cargo(self):
        return Man()  # Volvo, Scania

    def create_tank(self):
        return Abrams()   # Tiger, Merkava


def client(factory: AbstractCarFactory):
    vehicle = factory.create_vehicle()
    cargo = factory.create_cargo()
    tank = factory.create_tank()

    vehicle.drive()
    cargo.drive()
    tank.drive()


if __name__ == "__main__":
    client_number = input("Enter client number (0 - Default, 1 - FirstClient): ")

    clients = {
        0: DefaultCarFactory(),
        1: FirstClientCarFactory()
    }

    if client_number.isdigit() and int(client_number) in clients:
        factory = clients[int(client_number)]
        client(factory)
    else:
        print("Incorrect input")
