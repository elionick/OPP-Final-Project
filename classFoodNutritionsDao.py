import requests


class FoodNutritionsDao:
    url_main = "https://trackapi.nutritionix.com/"
    function_url = "v2/natural/nutrients"
    url = url_main + function_url
    num = 200
    appid = ["125860af", "76591b82", "966b1cc8","f6661396"]
    key = ["e1945fd53a59a5536c1f3d8daf69bb8e", "0c54d652d52dd4e0839a3a8e4c10930c", "f56ab2ebf3e2b1919c68c2ac0c2fa6f1","4477702c0fc88bcc6ba8a6e274b64994"]

    if num < 200:
        headers = {"x-app-id": appid[0], "x-app-key": key[0]}
    else:
        headers = {"x-app-id": appid[3], "x-app-key": key[3]}

    if num >= 400:
        num = 0

    @staticmethod
    def checkFoodInApi(food):
        FoodNutritionsDao.num += 1
        params = {"query": food}
        r = requests.post(FoodNutritionsDao.url,
                          headers=FoodNutritionsDao.headers, json=params).json()
        if 'foods' in r:
            return True
            #return r['foods'][0]['food_name']
        else:
            return False

if __name__ == "__main__":
    pass
