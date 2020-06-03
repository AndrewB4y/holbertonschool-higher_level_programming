#!/usr/bin/python3

""" add_attribute module """


def add_attribute(obj, att_name, att_value):
    """ add_attribute function """

    if type(obj).__module__ != "builtins":
        setattr(obj, att_name, att_value)
    else:
        raise TypeError("can't add new attribute")
