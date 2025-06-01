from shape import Shape
from visitor import ShapeVisitor


class Torus(Shape):
    def __init__(self, major_radius, minor_radius):
        self.major_radius = major_radius
        self.minor_radius = minor_radius

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_torus(self)
