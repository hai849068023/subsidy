import os
import json

small = {
    'appid': '',
    'appsecret': ''
}

path = os.path.abspath(os.path.dirname(__file__))
with open('{}/auth/city_code.json'.format(path), 'r', encoding='utf8') as f:
    city_code = json.load(f)