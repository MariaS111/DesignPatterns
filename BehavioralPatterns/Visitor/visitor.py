from abc import ABC, abstractmethod


class ShapeVisitor(ABC):
    @abstractmethod
    def visit_sphere(self, sphere):
        pass

    @abstractmethod
    def visit_parallelepiped(self, parallelepiped):
        pass

    @abstractmethod
    def visit_torus(self, torus):
        pass

    @abstractmethod
    def visit_cube(self, cube):
        pass


