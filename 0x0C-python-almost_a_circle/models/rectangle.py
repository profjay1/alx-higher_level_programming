#!/usr/bin/python3
''' Module for Rectangle class '''
from models.base import Base


class Rectangle(Base):
    ''' Representation of a Rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Constructor '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_value("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_value("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_value("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_value("y", value)
        self.__y = value

    def validate_value(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        ''' Calculates the area of the Rectangle instance '''
        return self.width * self.height

    def display(self):
        ''' Prints in stdout the Rectangle instance '''
        render = '\n' * self.y + \
                 (' ' * self.x + '#' * self.width + '\n') * self.height
        print(render, end="")

    def __str__(self):
        ''' Returns string info about the Rectangle instance '''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        ''' Internal method that updates instance attributes '''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        ''' Update the Rectangle attributes '''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of Rectangle '''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
