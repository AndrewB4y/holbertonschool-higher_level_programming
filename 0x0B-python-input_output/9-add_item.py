#!/usr/bin/python3

""" 9-add_item module """


if __name__ == "__main__":

    import sys
    import json

    save_to_json_file = __import__('7-save_to_json_file')
    load_from_json_file = __import__('8-load_from_json_file')

    input = sys.argv
    to_save = input[1:]
    j_file = load_from_json_file('add_item.json')
