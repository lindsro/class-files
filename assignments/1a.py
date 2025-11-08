import requests

url = 'https://www.loc.gov'

resource_id = ['/resource/ds.06560/', '/resource/ppmsca.18016/', '/resource/mss85943.002606/', '/resource/cph.3f05183/']

# params = {
#     'fo' : 'json'
# }

for resource in resource_id:
    r = requests.get(url + resource)
    print (r.status_code)
    print (r.url)