#!/usr/bin/python3

""" 5-hbtn_header module """

import requests
import sys

v = sys.argv
r = requests.get(v[1])
print(r.headers['X-Request-Id'])
