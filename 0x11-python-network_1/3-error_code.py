#!/usr/bin/python3

""" 3-error_code module """

if __name__ == "__main__":
    import urllib
    import sys

    v = sys.argv

    try:
        with urllib.request.urlopen(v[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
