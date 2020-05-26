#!/usr/bin/python3

"""4-print_square module

This module has only one function that prints a square with the character #.

Example:

>>> print_square = __import__('4-print_square').print_square
>>> print_square(4)
####
####
####
####
>>> print_square(10)
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
"""


def print_square(size):

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    if size > 0:
        for i in range(size):
            for j in range(size):
                print("#", end='')
            if i < size - 1:
                print()
    print()
