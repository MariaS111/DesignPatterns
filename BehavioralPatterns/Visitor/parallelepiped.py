from shape import Shape
from visitor import ShapeVisitor


class Parallelepiped(Shape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_parallelepiped(self)
