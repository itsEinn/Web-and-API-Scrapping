import requests
import json

#      TR      <API_ROOT_URL> yerine çekmek istediğiniz API'nin root URL'sini yazın
#    ENG     Replace <API_ROOT_URL> with the root URL of the API you want to scrape
api_root_url = "<API_ROOT_URL>"

response = requests.get(api_root_url)

response_json = json.loads(response.content)

endpoints = []

for key in response_json.keys():
    if isinstance(response_json[key], dict):
        for subkey in response_json[key].keys():
            endpoint = f"{key}/{subkey}"
            endpoints.append(endpoint)

# Print all available endpoints
for endpoint in endpoints:
    print(endpoint)
