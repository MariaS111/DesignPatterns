from abc import ABC, abstractmethod


class ISing(ABC):
    @abstractmethod
    def sing(self):
        pass


class IDance(ABC):
    @abstractmethod
    def dance(self):
        pass


class IWalk(ABC):
    @abstractmethod
    def walk(self):
        pass


class IProduceEgg(ABC):
    @abstractmethod
    def produce_egg(self):
        pass


class IDefendEgg(ABC):
    @abstractmethod
    def defend_egg(self):
        pass


class ISearchForSpouse(ABC):
    @abstractmethod
    def search_for_spouse(self):
        pass


class IFly(ABC):
    @abstractmethod
    def fly(self):
        pass
