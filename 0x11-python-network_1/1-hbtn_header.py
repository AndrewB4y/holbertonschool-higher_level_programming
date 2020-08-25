#!/usr/bin/python3

""" 1-hbtn_header module """
if __name__ == "__main__":
    import urllib.request
    import sys

    v = sys.argv
    with urllib.request.urlopen(v[1]) as response:
        print(response.headers.get('X-Request-Id'))
