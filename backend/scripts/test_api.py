import json
from urllib.request import Request, urlopen

def post(path, payload):
    url = f'http://127.0.0.1:8000{path}'
    data = json.dumps(payload).encode()
    req = Request(url, data=data, headers={'Content-Type':'application/json'})
    try:
        res = urlopen(req)
        print(path, res.status, res.read().decode())
    except Exception as e:
        print(path, 'error', e)

if __name__ == '__main__':
    post('/register', {'username':'smoketest3','password':'pass123','email':'smoke3@example.com'})
    post('/login', {'username':'smoketest3','password':'pass123'})
