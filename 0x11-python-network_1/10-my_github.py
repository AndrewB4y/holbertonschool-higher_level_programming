#!/usr/bin/python3

""" 10-my_github module """

import requests
import sys

v = sys.argv
""" first arg v[1] is the username, the second v[2] is de token"""
ba_auth = requests.auth.HTTPBasicAuth(v[1], v[2])
r = requests.get('https://api.github.com/user', auth=ba_auth)
print(r.json()['id'])
