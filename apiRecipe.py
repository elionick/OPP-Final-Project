import requests
import pprint
import pymysql


connection = pymysql.connect(host='sql7.freemysqlhosting.net',
                             port=3306,
                             user='sql7288305',
                             password='rEGuleh6A7',
                             db='sql7288305',
                             charset='latin1',
                             cursorclass=pymysql.cursors.DictCursor)

def food_nutrition(query):
    #api to get calories
    url_main = "https://trackapi.nutritionix.com/"
    function_url = "v2/natural/nutrients"
    url = url_main + function_url
    headers = {"x-app-id": "76591b82", "x-app-key": "0c54d652d52dd4e0839a3a8e4c10930c"}
    params = {"query" : query}
    r = requests.post(url, headers = headers, json = params)
    test = r.json()
    #print(test)
    """name = list()
    i = 0
    while i < len(test['foods']):
        name.append(test['foods'][i]['food_name'])
        i += 1"""
    calories = list()
    i = 0
    while i < len(test['foods']):
        calories.append(test['foods'][i]['nf_calories'])
        i += 1
    #print(calories)
    global calories_1
    calories_1 = sum(calories)
    #pprint.pprint(r.json())
    #need a solution –> no result found for the query



def getRecipeByMeal(USER_ID, INTOLERANCE, DIET):
    query = input("Search for meal")
    if (DIET == ""):

        r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?intolerances="+INTOLERANCE+"&number=20&offset=0&type=main+course&query="+query+"",
        headers={
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
        }
        )
    else:
        r = requests.get(
            "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?diet="+DIET+"&intolerances="+INTOLERANCE+"&number=20&offset=0&type=main+course&query="+query+"",
            headers={
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
            }
            )
    Result = r.json()
    Results = Result['results']
    #pprint.pprint(Results)
    names = list()
    i = 0
    while i < len(Results):
        names.append(Results[i]['title'])
        i += 1
    print(names)
    Ingredients_list = list()

    j = 0
    while j < len(Results):
        getRecipeIngedients(str(Results[j]['id']))
        Ingredients_list.append(INGREDIENTS1)
        j += 1

    number = list(range(1, (len(Results) + 1), 1))

    k = 0
    while (k < (len(Results))):
        summary = list()
        #print(Results[k]['image'])
        summary.extend((number[k], names[k], Ingredients_list[k]))
        print(summary)
        k += 1
    Recipe1 = int(input("Which of the dishes do you wanna choose? (number 1- " + str(len(Results)) + ")"))
    global Recipe_ID
    Recipe_ID = str(Results[Recipe1 - 1]['id'])
    global INGREDIENTS
    INGREDIENTS = Ingredients_list[Recipe1 - 1]
    #INGREDIENTS = INGREDIENTSX.replace("', '", ",")
    print(INGREDIENTS)
    global RECIPE_NAME
    RECIPE_NAME = str(names[Recipe1 - 1])
    global CALORIES
    i = 0
    calories = list()
    while (i < (len(Ingredients_list[Recipe1 - 1]))-1):
        food_nutrition(INGREDIENTS[i])
        calories.append(calories_1)
        i += 1
    print(calories)
    CALORIES = int(sum(calories))
    print(CALORIES)
    getRecipeInformation(Recipe_ID)

    test_fav = input("Do you wanna save the recipe in your favourites? yes/no")
    if (test_fav == "yes"):
        dbNewFav(connection, Recipe_ID, RECIPE_NAME, RECIPE, USER_ID, INGREDIENTS,CALORIES)
    else:
        choice2 = input("Do you want to search for another recipe? yes/no")
        if (choice2 == "yes"):
            getRecipeByIngredients()
        else:
            exit()


def getRecipeByIngredients(USER_ID):
    #search recipe by ingredients, option to save them in the Fav_recipe DB
    query = input("Insert the ingredients")

    r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=20&ranking=1&ignorePantry=false&ingredients="+query+"",
            headers={
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
            }
            )
    Results = r.json()
    names = list()
    i = 0
    while i < len(Results):
        names.append(Results[i]['title'])
        i += 1
    Ingredients_list = list()
    j = 0
    while j < len(Results):
        i = 0
        recipe_Ing = list()
        while i < len(Results[j]['missedIngredients']):
            recipe_Ing.append(Results[j]['missedIngredients'][i]['original'])
            i += 1
        i = 0
        while i < len(Results[j]['usedIngredients']):
            recipe_Ing.append(Results[j]['usedIngredients'][i]['original'])
            i += 1
        Ingredients_list.append(recipe_Ing)
        j += 1

    number = list(range(1,(len(Results)+1),1))

    k = 0
    while (k < (len(Results))):
        summary = list()
        print(Results[k]['image'])
        #Image.open(Results[k]['image']).show()
        summary.extend((number[k],names[k],Ingredients_list[k]))
        print(summary)
        k += 1
    #pprint.pprint(Results)
    Recipe1 = int(input("Which of the dishes do you want to choose? (number 1- "+str(len(Results))+")"))
    global Recipe_ID
    Recipe_ID = str(Results[Recipe1-1]['id'])
    global INGREDIENTS
    INGREDIENTS = Ingredients_list[Recipe1-1]
    print(INGREDIENTS)
    global RECIPE_NAME
    RECIPE_NAME = str(names[Recipe1-1])
    global CALORIES
    i = 0
    calories = list()
    while (i < (len(INGREDIENTS))):
        food_nutrition(INGREDIENTS[i])
        calories.append((int(calories_1)))
        i += 1
    CALORIES = int(sum(calories))
    print("Calories:"+str(CALORIES))
    getRecipeInformation(Recipe_ID)

    test_fav = input("Do you wanna save the recipe in your favourites? yes/no")
    if (test_fav == "yes"):
        dbNewFav(connection, Recipe_ID, RECIPE_NAME, RECIPE, USER_ID, INGREDIENTS, CALORIES)
    else:
        choice2 = input("Do you want to search for another recipe? yes/no")
        if (choice2 == "yes"):
            getRecipeByIngredients()
        else:
            exit()

def getRecipeIngedients(Recipe_ID):
    #api to get recipe ingredients
    response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+Recipe_ID+"/ingredientWidget.json",
                           headers={
                               "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                               "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
                           }
                           )
    #pprint.pprint(response.json())
    Recipe2 = response.json()
    i = 0
    if 'status' in Recipe2:
        ingredients1 = "No recipe"
    else:
        ingredients1 = list()
        while i < (len(Recipe2['ingredients'])-1):
            ingredient = str(Recipe2['ingredients'][i]['amount']['metric']['value']) + " " + Recipe2['ingredients'][i]['amount']['metric']['unit'] + " " + Recipe2['ingredients'][i]['name']
            ingredients1.append(ingredient)
            i += 1
        #print(ingredients1)
    global INGREDIENTS1
    INGREDIENTS1 = ingredients1

def getRecipeInformation(Recipe_ID):
    #api to get recipe for the choosen meal
    response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+Recipe_ID+"/information",
                           headers={
                               "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                               "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
                           }
                           )
    #pprint.pprint(response.json())
    Recipe2 = response.json()
    if (Recipe2 == "{'code': 404,'message': 'A recipe with the id "+Recipe_ID+" does not exist.','status': 'failure'}"):
        print("couldn't find the recipe")
        choice3 = input("Do you want to search for another recipe? yes/no")
        if (choice3 == "no"):
            exit()
        else:
            getRecipeByIngredients()
    else:
        global RECIPE
        RECIPE = str(Recipe2['instructions'])
        pprint.pprint(RECIPE)





def dbInfoUser(connection, USER_ID):
    try:
        with connection.cursor() as cursor:
            sql = "select USER_ID,LOGIN_NAME,FIRST_NAME,LAST_NAME,cast(BIRTHDATE as char) AS BIRTHDAY ,HEIGHT,WEIGHT,DIET,INTOLERANCE FROM USER WHERE USER_ID = %s"
            cursor.execute(sql, USER_ID)
            output = cursor.fetchone()
            global HEIGHT
            HEIGHT = output['HEIGHT']
            global WEIGHT
            WEIGHT = output['WEIGHT']
            global DIET
            DIET = output['DIET']
            global INTOLERANCE
            INTOLERANCE = output['INTOLERANCE']

    finally:
            cursor.close()

def dbNewFav(connection, Recipe_ID, RECIPE_NAME, RECIPE,USER_ID, INGREDIENTS, CALORIES):
    #adds new entry to the FAV_RECIPE table
    try:
        with connection.cursor() as cursor:
           # CALORIES = input("CALORIES")
            #PRICE = input("PRICE")
            #ALLEGIES = input("ALLEGIES")
            #INTOLERANCE = input("INTOLERANCE")
            sql = "INSERT INTO FAV_RECIPE (RECIPE_ID,RECIPE_NAME,RECIPE,USER_ID, INGREDIENTS, CALORIES)"\
             + "VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (Recipe_ID,RECIPE_NAME,RECIPE,USER_ID,str(INGREDIENTS),CALORIES))
            connection.commit()
            print("insert successful")

    finally:
        cursor.close()



if __name__ == '__main__':

    #dbLogin()
    #getRecipeIngedients("849492")
    #connection.close()
    #getRecipeInformation("849492")
    #getRecipeByMeal(1,"","no")
    getRecipeByIngredients(1)
    #food_nutrition("i ate 2 eggs, ten strawberries, and 10 french toast")
