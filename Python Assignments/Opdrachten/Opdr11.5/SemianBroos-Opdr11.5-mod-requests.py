import requests

r = requests.get('https://w3schools.com/python/demopage.htm')
code = r.status_code
if code == 200:
    hd = r.headers['content-type']
    enc = r.encoding
    t = r.text
    #js = r.json()
    print(t)
else:
    print('error ', code)