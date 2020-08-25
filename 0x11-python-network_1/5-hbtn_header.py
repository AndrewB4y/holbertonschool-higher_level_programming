#!/usr/bin/python3

""" 5-hbtn_header module """

if __name__ == "__main__":
    import requests
    import sys

    v = sys.argv
    r = requests.get(v[1])
    print(r.headers.get('X-Request-Id'))
