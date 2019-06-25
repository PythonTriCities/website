#!/usr/bin/env python3
import urllib.request
needle = b'Python Tri Cities Website'
req = urllib.request.Request('http://localhost:5000')

with urllib.request.urlopen(req) as response:
    haystack = response.read()
    if needle in haystack:
        print('Passed')
    else:
        print('Failed')
