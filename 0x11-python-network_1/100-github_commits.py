#!/usr/bin/python3

""" 100-github_commits module """

if __name__ == '__main__':
    import requests
    import sys

    v = sys.argv
    s = 'https://api.github.com/repos/{}/{}/commits?per_page=10'
    r = requests.get(s.format(v[2], v[1]))
    ans = r.json()
    for c in ans:
        print("{}: {}".format(c.get('sha'),
                              c.get('commit').get('author').get('name')))
