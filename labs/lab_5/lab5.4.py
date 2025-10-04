import requests
import json

url = 'https://www.loc.gov'

search_endpoint = '/search/'

query = input("What would you like to search?")

params = {'q' : query,
          'fo': 'json'
          }

r = requests.get(url + search_endpoint, params=params)
print (r.url)
print('Writing your result...\n')
with open(f'{query}_result.json','w',encoding='utf-8') as f:
    json.dump(json.loads(r.text), f, indent=2)