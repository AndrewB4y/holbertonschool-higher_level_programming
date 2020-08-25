#!/usr/bin/python3

""" 8-json_api module """


if __name__ == "__main__":
    import requests
    import sys

    v = sys.argv
    q = ""
    if len(v) > 1:
        q = v[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        ans = r.json()
        if ans == {}:
            print("No result")
        else:
            print("[{}] {}".format(ans.get('id'), ans.get('name')))
    except:
        print("Not a valid JSON")
