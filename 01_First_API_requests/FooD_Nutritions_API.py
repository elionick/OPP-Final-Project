import requests
import json
import pprint
url_main = "https://trackapi.nutritionix.com/"
function_url = "v2/natural/nutrients"
query = "i ate 2 eggs, ten bacon, and 2 french toast"
url = url_main + function_url
headers = {"x-app-id": "76591b82", "x-app-key": "0c54d652d52dd4e0839a3a8e4c10930c"}
params = {"query" : query}
r = requests.post(url, headers = headers, json = params)
pprint.pprint(r.json())