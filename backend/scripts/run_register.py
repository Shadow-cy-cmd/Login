import json
import sys
from urllib.request import Request, urlopen

API = 'http://127.0.0.1:8000'

def post(path, payload):
    url = API + path
    req = Request(url, data=json.dumps(payload).encode(), headers={'Content-Type':'application/json'})
    try:
        res = urlopen(req, timeout=10)
        print(path, res.status, res.read().decode())
    except Exception as e:
        print(path, 'error', e)

if __name__ == '__main__':
    username = sys.argv[1] if len(sys.argv) > 1 else 'pramod'
    password = sys.argv[2] if len(sys.argv) > 2 else '123456'
    email = sys.argv[3] if len(sys.argv) > 3 else 'use133282@gmail.com'
    post('/register', {'username': username, 'password': password, 'email': email})
    post('/login', {'username': username, 'password': password})
