import requests

url = 'https://www.loc.gov'
lccn_url = 'https://lccn.loc.gov/98508155'

resource_id = ['/resource/cph.3f05183', '/resource/fsa.8d24709/', '/resource/highsm.64003/']

parameters = {
    'fo' : 'json'
}
for resource in resource_id:
    r = requests.get(url + resource, parameters)
    print (r.url)
    # print (r.headers)

# print (r)
# print (r.url)
# print (r.status_code)
# print (r.headers)

# print (r.text)
# print (r.json)

for header in r.headers:
    print (header, ':' ,r.headers[header])

