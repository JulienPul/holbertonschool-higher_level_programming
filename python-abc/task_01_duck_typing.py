#!/usr/bin/python3
"""module Shapes, Interfaces, and Duck Typing"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return abs(2 * math.pi * self.radius)


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return ((self.width + self.height) * 2)


def shape_info(Shape):
    area = Shape.area()
    perimeter = Shape.perimeter()
    print(f"Area: {(area)}")
    print(f"Perimeter: {(perimeter)}")
