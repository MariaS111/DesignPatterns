from abc import ABC, abstractmethod


# Wrong
class Animal:
    def fly(self):
        print('Fly')

    def swim(self):
        print('Swim')


class Duck(Animal):
    def fly(self):
        print("Duck is flying")


class Dog(Animal):
    def fly(self):
        raise NotImplementedError("Dogs can't fly")


# Right
class IFly(ABC):
    @abstractmethod
    def fly(self):
        pass


class ISwim(ABC):
    @abstractmethod
    def swim(self):
        pass


class Duck(IFly, ISwim):
    def fly(self):
        print("Duck is flying")

    def swim(self):
        print("Duck is swimming")


class Dog(ISwim):
    def swim(self):
        print("Dog is swimming")
