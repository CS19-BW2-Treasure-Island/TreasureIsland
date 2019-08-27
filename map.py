import requests
import json

headers = {
    'Authorization': 'Token 8462b8d16624f572bdc0d8402680ae5245449f4d',
    'Content-Type': 'application/json',
}

north = '{"direction":"n"}'
south = '{"direction":"s"}'
east = '{"direction":"e"}'
west = '{"direction":"w"}'

get = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers)
post = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=east)
