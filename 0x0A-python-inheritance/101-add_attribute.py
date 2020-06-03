#!/usr/bin/python3

""" add_attribute module """


def add_attribute(obj, att_name, att_value):
    """ add_attribute function """

    if obj.__class__.__module__ == 'builtins':
        raise TypeError("can't add new attribute")

    setattr(obj, att_name, att_value)
