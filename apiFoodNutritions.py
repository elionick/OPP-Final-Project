import requests

class apiFoodNutritions:
    url_main = "https://trackapi.nutritionix.com/"
    function_url = "v2/natural/nutrients"
    url = url_main + function_url
    appids = ["bce0b0b5", "125860af", "76591b82", "966b1cc8","f6661396"]
    keys = ["e7c0ea3cc865c376372b54a51856ae54", "e1945fd53a59a5536c1f3d8daf69bb8e", "0c54d652d52dd4e0839a3a8e4c10930c", "f56ab2ebf3e2b1919c68c2ac0c2fa6f1", "4477702c0fc88bcc6ba8a6e274b64994"]
    
    @staticmethod
    def getHeader():
        for index, appid in enumerate(apiFoodNutritions.appids):
            headers = {"x-app-id": appid, "x-app-key": apiFoodNutritions.keys[index]}
            params = {"query" : "Apple"}
            r = requests.post(apiFoodNutritions.url, headers = headers, json = params).json()
            try:
                if r['message'] == 'usage limits exceeded':
                    pass
            except:
                break
        return headers
    
    @staticmethod
    def apiFoodNutritions(food):
        params = {"query" : food}
        r = requests.post(apiFoodNutritions.url, headers = apiFoodNutritions.getHeader(), json = params).json()
        if 'foods' in r:
            return True
        else:
            return False
    
    @staticmethod
    def checkFoodInApi(food):
        params = {"query" : food}
        r = requests.post(apiFoodNutritions.url, headers = apiFoodNutritions.getHeader(), json = params).json()
        if 'foods' in r:
            return True
        else:
            return False
    
    @staticmethod
    def getCaloriesOfFood(food):
        params = {"query" : food}
        r = requests.post(apiFoodNutritions.url, headers = apiFoodNutritions.getHeader(), json = params).json()
        sum_calories = 0
        for element in r['foods']:
            sum_calories += element['nf_calories']
        return sum_calories
    
    @staticmethod
    def getFoodNameString(food):
        if food == "":
            return ""
        food_names = []
        for food in food.split(","):
            params = {"query" : food}
            r = requests.post(apiFoodNutritions.url, headers = apiFoodNutritions.getHeader(), json = params).json()
            for element in r['foods']:
                food_names.append(element['tags']['item'])
            retv = ", ".join(food_names)
        return retv
    
    @staticmethod
    def getFoodNameList(food):
        food_names = []
        for food in food.split(","):
            params = {"query" : food}
            r = requests.post(apiFoodNutritions.url, headers = apiFoodNutritions.getHeader(), json = params).json()
            for element in r['foods']:
                food_names.append(element['tags']['item'])
        return list(set(food_names))

    @staticmethod
    def getCalories(query):
        try:
            params = {"query": query}
            r = requests.post(apiFoodNutritions.url, headers=apiFoodNutritions.getHeader(), json=params)
            test = r.json()
            # pprint.pprint(test)
            name = list()
            i = 0
            while i < len(test['foods']):
                name.append(test['foods'][i]['food_name'])
                i += 1
            calories = list()
            i = 0
            while i < len(test['foods']):
                calories.append(test['foods'][i]['nf_calories'])
                i += 1
            return (int(sum(calories)))
        except Exception:
            return (0)

if __name__ == "__main__":
    pass