import requests
import pprint

def food_nutrition(query):
    try:
        url_main = "https://trackapi.nutritionix.com/"
        function_url = "v2/natural/nutrients"
        url = url_main + function_url
        headers = {"x-app-id": "966b1cc8", "x-app-key": "f56ab2ebf3e2b1919c68c2ac0c2fa6f1"}
        params = {"query": query}
        r = requests.post(url, headers=headers, json=params)
        test = r.json()
        #pprint.pprint(test)
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
    #pprint.pprint(r.json())



if __name__ == '__main__':
    pass
    #t1 = Recipe_Class("i ate 2 eggs, ten strawberries, and 10 french toast")
    #t1.getCalories

    #print("i ate 2 eggs, ten strawberries, and 10 french toast")
    #food_nutrition("i ate 2 eggs, ten strawberries, and 10 french toast")