import requests
import json
import pprint

# BMI
url_main = "https://gabamnml-health-v1.p.rapidapi.com/bmi?"
weight = 60
height = 1.70
url = url_main + "weight=" + str(weight) + "&height=" + str(height)
r = requests.get(url,
  headers={
    "X-RapidAPI-Host": "gabamnml-health-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "c7221509d3mshcbb2389951ffc2ap1edf91jsn4a622dc8442c"
  }
)
pprint.pprint(r.json())


