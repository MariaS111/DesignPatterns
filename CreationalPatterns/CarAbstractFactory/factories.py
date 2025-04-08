from abc import abstractmethod, ABC
from vehicle import Vehicle, Audi, Honda, Tesla
from cargo import Cargo, Volvo, Man, Scania
from tank import Tank, Tiger, Abrams, Merkava



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


class SecondClientCarFactory(AbstractCarFactory):
    def create_vehicle(self):
        return Tesla()  # Audi, Honda

    def create_cargo(self):
        return Scania()  # Volvo, Man

    def create_tank(self):
        return Merkava()  # Tiger, Abrams