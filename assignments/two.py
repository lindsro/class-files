import json
import requests
import csv
from pathlib import Path

base_url = " https://www.loc.gov/free-to-use/libraries/"
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

# def create_collection_list(json_path, csv_path):
#     with open(json_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     # Check if 'items' is at the top-level, if not, look for it in related structure
#     items = data.get('results') or data.get('items') or []  # Fallback for known keys

#     print(f"Total items found: {len(items)}")

#     with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['title', 'link', 'image'])  # headers

#         for item in items:
#             title = item.get('title', '')
#             link = item.get('id', '') # Sometimes URL link is here; adjust as needed
#             # Sometimes image url is under different keys; find the one that works:
#             image = ''
#             if 'image_url' in item:
#                 image = item['image_url'][0] if item['image_url'] else ''
#             elif 'image' in item:
#                 image = item['image'][0] if item['image'] else ''
#             elif 'resources' in item and item['resources']:
#                 image = item['resources'][0].get('image', '')
#             writer.writerow([title, link, image])

#     print(f"Saved CSV to {csv_path}")