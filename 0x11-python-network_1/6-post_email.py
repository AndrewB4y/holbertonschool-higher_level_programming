#!/usr/bin/python3

"""  6-post_email module """

if __name__ == "__main__":
    import requests
    import sys

    v = sys.argv
    r = requests.post(v[1], data={'email': v[2]})
    print(r.text)
