#!/usr/bin/python3


class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for k in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            if i < self.__size - 1:
                print()
        print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
