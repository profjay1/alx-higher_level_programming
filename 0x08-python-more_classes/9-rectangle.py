#!/usr/bin/python3
""" Module for Rectangle class. """


class Rectangle:
    """
    Representation of a Rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialization """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        """ Returns string representation with '#' """
        if not self.__width or not self.__height:
            return ""
        w = self.width
        h = self.height
        return ((str(self.print_symbol) * w + '\n') * h)[:-1]

    def __repr__(self):
        """ Returns formal string representation """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """ Destructor """
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @property
    def width(self):
        """ width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the area of the Rectangle """
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the bigger of two rectangles.
        Args:
            rect_1: The first rectangle.
            rect_2: The second rectangle.
        Raises:
            TypeError: If rect_1, rect_2 are not instances of Rectangle.
        Returns:
            The rectangle with the larger area.
        '''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Initializes a new square
        """
        return cls(size, size)
