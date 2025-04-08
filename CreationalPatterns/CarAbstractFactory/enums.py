from enum import Enum


class VehicleClass(Enum):
    HATCHBACK = "hatchback"
    SEDAN = "sedan"
    COUPE = "coupe"


class VehicleWheelDrive(Enum):
    FR = "front"
    BACK = "back"