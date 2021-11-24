import sys
import os
from math import pi

class Circle():
    def __init__(self, radius, fill='red',stroke='black'):
        self._radius = radius
        self._fill = fill
        self._stroke = stroke

    def calculate_area(self):
        """Calculates the area"""
        return pi + self._radius ** 2

    @property # public access for _radius: read-only
    def radius(self):
        return self._radius
    
    @property
    def fill(self):
        return self._fill

    @property
    def stroke(self):
        return self._stroke

    def __len__(self):
        return int(2 * pi * self._radius ** 2)

    def __str__(self):
        return f'Instance of {self.__class__.__qualname__}'

    def __repr__(self):
        return f'Circle({self.radius}, fill={self.fill}, stroke={self.stroke})'

class Quadrilateral():
    def __init__(self, height, width, fill='pink',stroke='black'):
        self._height = height
        self._width = width
        self._fill = fill
        self._stroke = stroke

    def calculate_area(self):
        """Calculates the area"""
        return self._height * self._width

class Canvas():
    def __init__(self, height, width, bg):
        self._height = height
        self._width = width
        self._bg = bg
      
class Text():
    def __init__(self, size, colour, font):
        self._size = size
        self._colour = colour
        self._font = font

def main():
    circle = Circle(5.0, fill='orange', stroke='black')
    print(str(circle)) #Example of Dunder methods

    print(repr(circle))

    print(circle._radius)
    #circle.radius = 5 #won't work (can't overwrite private variable since property was set)
    circle._radius = 5
    print(f'area = {circle.calculate_area}')
    return 0
    #return os.EX_OK

if __name__ == "__main__":
    main()

