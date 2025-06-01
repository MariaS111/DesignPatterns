from visitor import ShapeVisitor
from volume_visitor import VolumeVisitor
from cube import Cube
from parallelepiped import Parallelepiped
from torus import Torus
from sphere import Sphere
from typing import List
from shape import Shape


def main(shapes: List[Shape], visitor: ShapeVisitor):
    for shape in shapes:
        shape.accept(visitor)


if __name__ == "__main__":
    shapes = [
        Sphere(3),
        Parallelepiped(2, 4, 6),
        Torus(5, 1.2),
        Cube(3)
    ]

    visitor = VolumeVisitor()
    main(shapes, visitor)

