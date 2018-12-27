import urllib.request
test_str = b'Python Tri Cities Website'
req = urllib.request.Request('http://localhost:5000')

with urllib.request.urlopen(req) as response:
    page = response.read()
    if test_str in page:
        print('Passed')
    else:
        print('Failed')
