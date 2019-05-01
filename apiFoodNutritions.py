import requests

class apiFoodNutritions:
    url_main = "https://trackapi.nutritionix.com/"
    function_url = "v2/natural/nutrients"
    url = url_main + function_url
    # headers = {"x-app-id": "76591b82", "x-app-key": "0c54d652d52dd4e0839a3a8e4c10930c"}
    headers = {"x-app-id": "bce0b0b5", "x-app-key": "e7c0ea3cc865c376372b54a51856ae54"}
    
    @staticmethod
    def apiFoodNutritions(food):
        params = {"query" : food}
        r = requests.post(apiFoodNutritions.url, headers = apiFoodNutritions.headers, json = params).json()
        if 'foods' in r:
            return True
        else:
            return False
    
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
    
    @staticmethod
    def getFoodNameString(food):
        food_names = []
        for food in food.split(","):
            params = {"query" : food}
            r = requests.post(apiFoodNutritions.url, headers = apiFoodNutritions.headers, json = params).json()
            for element in r['foods']:
                food_names.append(element['tags']['item'])
            retv = ", ".join(food_names)
        return retv
    
    @staticmethod
    def getFoodNameList(food):
        food_names = []
        for food in food.split(","):
            params = {"query" : food}
            r = requests.post(apiFoodNutritions.url, headers = apiFoodNutritions.headers, json = params).json()
            for element in r['foods']:
                food_names.append(element['tags']['item'])
        return list(set(food_names))

if __name__ == "__main__":
    pass