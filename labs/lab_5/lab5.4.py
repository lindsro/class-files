import requests
import json

url = 'https://www.loc.gov'

search_endpoint = '/search/'

query = input("What would you like to search?")

params = {'q' : query}

r = requests.get(url + search_endpoint, params=params)
print (r.url)