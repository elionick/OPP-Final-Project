import requests


class FoodNutritionsDao:
    url_main = "https://trackapi.nutritionix.com/"
    function_url = "v2/natural/nutrients"
    url = url_main + function_url
    num = 0
    appid = ["125860af", "76591b82"]
    key = ["e1945fd53a59a5536c1f3d8daf69bb8e", "0c54d652d52dd4e0839a3a8e4c10930c"]

    if num < 200:
        headers = {"x-app-id": appid[0], "x-app-key": key[0]}
    else:
        headers = {"x-app-id": appid[1], "x-app-key": key[1]}

    if num >= 400:
        num = 0

    @staticmethod
    def checkFoodInApi(food):
        FoodNutritionsDao.num += 1
        params = {"query": food}
        r = requests.post(FoodNutritionsDao.url,
                          headers=FoodNutritionsDao.headers, json=params).json()
        if 'foods' in r:
            # return True
            return r['foods'][0]['food_name']
        else:
            return False

    def getCalories(query):
        try:
            headers = {"x-app-id": "966b1cc8", "x-app-key": "f56ab2ebf3e2b1919c68c2ac0c2fa6f1"}
            params = {"query": query}
            r = requests.post(FoodNutritionsDao.url, headers=headers, json=params)
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
