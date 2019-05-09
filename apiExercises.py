import requests

# Function for to get all available information from query
def getExerciseDataFromQuery(query, gender=None, weight_kg=None, height_cm=None, age=None):
    url_main = "https://trackapi.nutritionix.com/"
    function_url = "v2/natural/exercise"
    url = url_main + function_url
    headers = {"x-app-id": "76591b82", "x-app-key": "0c54d652d52dd4e0839a3a8e4c10930c"}
    params = {"query": query, "gender": gender,
              "weight_kg": weight_kg, "height_cm": height_cm, "age": age}
    retv = requests.post(url, headers=headers, json=params)
    return retv

# Function to get only exercise names of query (returns list)
def getExerciseName_s(query, gender=None, weight_kg=None, height_cm=None, age=None):
    r = getExerciseDataFromQuery(
        query, gender=gender, weight_kg=weight_kg, height_cm=height_cm, age=age)
    retv = []
    for index, _ in enumerate(r.json()['exercises']):
        retv.append(r.json()["exercises"][index]["name"])
    return retv

# Function to get calories burned by exercise (returns dictionary)
def getCaloriesBurnedByExercise(query, gender=None, weight_kg=None, height_cm=None, age=None):
    r = getExerciseDataFromQuery(
        query, gender=gender, weight_kg=weight_kg, height_cm=height_cm, age=age)
    retv = {exercise: r.json()["exercises"][index]["nf_calories"] for index, exercise in enumerate(
        getExerciseName_s(query, gender=gender, weight_kg=weight_kg, height_cm=height_cm, age=age))}
    return retv

# Function to get approx. duration of exercises in minutes by exercise
def getDurationByExercise(query, gender=None, weight_kg=None, height_cm=None, age=None):
    r = getExerciseDataFromQuery(
        query, gender=gender, weight_kg=weight_kg, height_cm=height_cm, age=age)
    retv = {exercise: r.json()["exercises"][index]["duration_min"] for index, exercise in enumerate(
        getExerciseName_s(query, gender=gender, weight_kg=weight_kg, height_cm=height_cm, age=age))}
    return retv

# Function to get calories burned by exercise (returns dictionary)
def getMetByExercise(query, gender=None, weight_kg=None, height_cm=None, age=None):
    r = getExerciseDataFromQuery(
        query, gender=gender, weight_kg=weight_kg, height_cm=height_cm, age=age)
    retv = {exercise: r.json()["exercises"][index]["met"] for index, exercise in enumerate(
        getExerciseName_s(query, gender=gender, weight_kg=weight_kg, height_cm=height_cm, age=age))}
    return retv


if __name__ == "__main__":
    pass
