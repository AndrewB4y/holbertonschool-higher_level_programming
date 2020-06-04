#!/usr/bin/python3

""" read_lines module """


def read_lines(filename="", nb_lines=0):
    """
    read_lines function

    reads n lines of a text file (UTF8) and prints it to stdout
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read())

        for n, line in enumerate(f.readlines()):
            if n >= nb_lines:
                break
            print(line, end='')
