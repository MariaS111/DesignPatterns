from visitor import ShapeVisitor
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: ShapeVisitor):
        pass
