from shape import Shape
from visitor import ShapeVisitor


class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_sphere(self)
