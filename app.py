import json
import requests

def get_init():
    url = ('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/')
    headers = {'Authorization' : 'Token a0243e3f1036125e5d2a0e5ffe7c64fcfa3bc126'}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return json.loads(r.text)
    else:
        return None

init_info = get_init()

if init_info is not None:
    print(f'here is the res {init_info}')
else:
    print('Error during request')





# api_token = 'a0243e3f1036125e5d2a0e5ffe7c64fcfa3bc126'
# api_url_base = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/'

# headers = {'Content-Type': 'application/json',
#             'Authorization': 'Bearer {0}'.format(api_token)}

# def get_init():

#     api_url = '{0}init/'.format(api_url_base)

#     response = requests.get(api_url, headers=headers)

#     if response.status_code == 200:
#         return json.loads(response.content.decode('uft-8'))
#     else:
#         return None

# account_info = get_init()

# if account_info is not None:
#     print(f'here is the res {account_info}')
#     # for k, v in account_info['account'].items():
#     #     print('{0} : {1}'.format(k, v))
# else:
#     print('[!] Request failed')