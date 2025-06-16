from abc import ABC, abstractmethod


# Wrong
class Shape:
    def __init__(self, shape_type: str):
        self.shape_type = shape_type

    def draw(self):
        if self.shape_type == "circle":
            print("Drawing circle")
        elif self.shape_type == "square":
            print("Drawing square")
        else:
            print("Unknown shape")


# Right
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Drawing circle")


class Square(Shape):
    def draw(self):
        print("Drawing square")


class ShapeRenderer:
    def __init__(self, shape: Shape):
        self.shape = shape

    def render(self):
        self.shape.draw()
