#!/usr/bin/python3
''' Module for Square class '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Representation of a Square '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Constructor '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' Returns string info about the Square instance '''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance attributes '''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        ''' Updates Square attributes '''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        ''' Dictionary representaton of Square '''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
