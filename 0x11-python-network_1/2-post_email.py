#!/usr/bin/python3

""" 2-post_email module """
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    v = sys.argv
    url = v[1]
    values = {'email': v[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('uft-8'))
