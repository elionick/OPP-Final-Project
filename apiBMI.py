import requests

# BMI


def getBMI(weight, height):
    # Extra key: c7221509d3mshcbb2389951ffc2ap1edf91jsn4a622dc8442c
    url_main = "https://gabamnml-health-v1.p.rapidapi.com/bmi?"
    url = url_main + "weight=" + str(weight) + "&height=" + str(height)
    headers = {
        "X-RapidAPI-Host": "gabamnml-health-v1.https://rapidapi.p.rapidapi.com",
        "X-RapidAPI-Key": "d6e7ff25d6mshfa2f6f852448b10p1f6388jsn27267db6bdc5"
    }
    retv = requests.get(url, headers=headers).json()["result"]
    return retv

# BMI status


def getBMIstatus(weight, height):
    url_main = "https://gabamnml-health-v1.p.rapidapi.com/bmi?"
    url = url_main + "weight=" + str(weight) + "&height=" + str(height)
    headers = {
        "X-RapidAPI-Host": "gabamnml-health-v1.https://rapidapi.p.rapidapi.com",
        "X-RapidAPI-Key": "d6e7ff25d6mshfa2f6f852448b10p1f6388jsn27267db6bdc5"
    }
    retv = requests.get(url, headers=headers).json()["status"]
    return retv
