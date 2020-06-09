#!/usr/bin/python3

""" rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        for s in range(self.y):
            print()
        for i in range(self.height):
            for s in range(self.x):
                print(end=' ')
            for j in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        msg = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return msg.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        if args != ():
            to_upd = {
                0: "id",
                1: "width",
                2: "height",
                3: "x",
                4: "y",
            }
            for n, value in enumerate(args):
                setattr(self, to_upd[n], value)
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        rep = {
            'id': 0,
            'width': 0,
            'height': 0,
            'x': 0,
            'y': 0
        }
        for k in rep:
            rep[k] = getattr(self, k)

        return rep
