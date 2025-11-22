import json
import requests
import csv
from pathlib import Path

base_url = " https://www.loc.gov/free-to-use"
params = {
    'fo' : 'json'
}

r = requests.get(base_url, params=params) # Now I can access the underlying json data and treat it like a dictionary!
print(r.status_code) # This is to make sure its working - 200 status is good and working correctly

if r.status_code == 200:
    with open('loclibset.json', 'w', encoding='utf-8') as f: # 'W' means open as a write file, can also use 'r' (read) or 'a' (append)
        f.write(r.text)
    print("Saved JSON to loclibset.json")
else:
    print('Error:', r.status_code)

collection = 'libraries'

collection_list_response = requests.get(base_url + '/' + collection, params=params)

print(collection_list_response.url)

collection_json = collection_list_response

collection_json = collection_list_response.json()

print(collection_json.keys())

for k in collection_json['content']['set']['items']:
    print(k)

len(collection_json['content']['set']['items'])

collection_json['content']['set']['items'][0].keys()

collection_set_list = '/collection-project/collection_set_list.csv'
headers = ['image', 'link', 'title']

with open(collection_set_list, 'w', encoding='utf-8', newline=' ') as f:
    writer = csv.DictWriter(f, fiednames=headers)
    writer.writeheader()
    for item in collection_json['content']['set']['items']:
        item['title'] = item['title'].rstrip()
        writer.writerow(item)
    print('wrote', collection_set_list)