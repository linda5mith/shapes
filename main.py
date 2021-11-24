import sys
import os
from math import pi
import yaml

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

    # def __str__(self):
    #     return f'Instance of {self.__class__.__qualname__}'

    def __repr__(self):
        return f'Circle({self.radius}, fill={self.fill}, stroke={self.stroke})'

    def __str__(self):
        string = yaml.dump({
            'circle':{
                'radius':self._radius,
                'fill':self._fill,
                'stroke':self._stroke
            }
        })
        return string
       # return f'Instance of {self.__class__.__qualname__}'

    # Deserialization: Class (static) methods
    @classmethod
    def from_yaml(cls,string):
        """Create a circle from a YAML string"""
        circle_dict = yaml.load(string, Loader=yaml.Loader)
        #print(circle_dict)
        obj = cls(circle_dict['radius'],fill=circle_dict['fill'],stroke=circle_dict['stroke'],at=circle_dict['at']) #cls stands in for name of class
        return obj

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

    my_dict = {
        'key':{
            'inside_dict':[5,6,7,8]
        }
    }

    print(yaml.dump(my_dict))

    yaml_circle = '''\
circle:
    at: !!python/tuple
    - 0
    - 0
    fill: orange
    radius: 5.0
    stroke: red'''
    my_circle = Circle.from_yaml(yaml_circle)

    return 0
    #return os.EX_OK

if __name__ == "__main__":
    main()

