import requests
import pprint
url_main = "https://trackapi.nutritionix.com/"
function_url = "v2/natural/exercise"
query = "I made 10 sit-ups"
gender = "male"
weight_kg = 72.5
height_cm = 167.64
age = 30

url = url_main + function_url
headers = {"x-app-id": "76591b82", "x-app-key": "0c54d652d52dd4e0839a3a8e4c10930c"}
params = {"query" : query, "gender" : gender, "weight_kg" : weight_kg, "height_cm" : height_cm, "age" : age}
r = requests.post(url, headers = headers, json = params)
pprint.pprint(r.json()['exercises'])