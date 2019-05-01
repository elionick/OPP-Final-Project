import requests

class apiFoodNutritions:
    url_main = "https://trackapi.nutritionix.com/"
    function_url = "v2/natural/nutrients"
    url = url_main + function_url
    headers = {"x-app-id": "76591b82", "x-app-key": "0c54d652d52dd4e0839a3a8e4c10930c"}
    
    @staticmethod
    def checkFoodInApi(food):
        params = {"query" : food}
        r = requests.post(apiFoodNutritions.url, headers = apiFoodNutritions.headers, json = params).json()
        if 'foods' in r:
            return True
        else:
            return False
    
    @staticmethod
    def getCaloriesOfFood(food):
        params = {"query" : food}
        r = requests.post(apiFoodNutritions.url, headers = apiFoodNutritions.headers, json = params).json()
        sum_calories = 0
        for element in r['foods']:
            sum_calories += element['nf_calories']
        return sum_calories



if __name__ == "__main__":
    pass