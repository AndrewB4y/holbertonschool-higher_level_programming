#!/usr/bin/python3

"""  6-post_email module """

import requests
import sys

v = sys.argv
r = requests.post(v[1], data={'email': v[2]})
print(r.text)
