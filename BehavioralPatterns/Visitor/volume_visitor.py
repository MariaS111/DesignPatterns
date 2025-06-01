from visitor import ShapeVisitor
from cube import Cube
from parallelepiped import Parallelepiped
from torus import Torus
from sphere import Sphere
import math


class VolumeVisitor(ShapeVisitor):
    def visit_sphere(self, sphere: Sphere):
        volume = (4/3) * math.pi * sphere.radius ** 3
        print(f"Sphere volume: {volume:.2f}")
        return volume

    def visit_parallelepiped(self, p: Parallelepiped):
        volume = p.length * p.width * p.height
        print(f"Parallelepiped volume: {volume:.2f}")
        return volume

    def visit_torus(self, torus: Torus):
        volume = (2 * math.pi ** 2) * torus.major_radius * torus.minor_radius ** 2
        print(f"Torus volume: {volume:.2f}")
        return volume

    def visit_cube(self, cube: Cube):
        volume = cube.side ** 3
        print(f"Cube volume: {volume:.2f}")
        return volume