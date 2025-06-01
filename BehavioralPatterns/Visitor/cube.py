from shape import Shape
from visitor import ShapeVisitor


class Cube(Shape):
    def __init__(self, side):
        self.side = side

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_cube(self)
