#!/usr/bin/python3

""" 7-error_code module """


if __name__ == "__main__":
    import requests
    import sys

    v = sys.argv

    r = requests.get(v[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
