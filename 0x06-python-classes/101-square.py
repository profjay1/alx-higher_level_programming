#!/usr/bin/python3
"""defines a Square Class"""


class Square:
    """Represents a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square"""
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """ this function prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for x in range(self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.__size))

    def str_representation(self):
        """returns the str representation of the square with the character #"""
        string = str()
        if self.__size == 0:
            return "\n"
        for i in range(self.__position[1]):
            string += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                string += " "
            for j in range(self.size):
                string += "#"
            string += "\n"
        return string

    def __str__(self):
        return self.str_representation()[:-1]
