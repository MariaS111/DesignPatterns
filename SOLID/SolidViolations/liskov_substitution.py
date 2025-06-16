from abc import ABC, abstractmethod


# Wrong
class Employee:
    def get_salary(self):
        return 5000


class PartTimeEmployee(Employee):
    def get_salary(self):
        raise Exception("Not supported")


# Right
class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass


class FullTimeEmployee(Employee):
    def get_salary(self):
        return 5000


class PartTimeEmployee(Employee):
    def __init__(self, worked_hours):
        self.worked_hours = worked_hours

    def get_salary(self):
        return 30 * self.worked_hours
