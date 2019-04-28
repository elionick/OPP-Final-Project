import requests
import pprint
import pymysql
from Food_Nutrition import *
from classFoodNutritionsDao import *


connection = pymysql.connect(host='sql7.freemysqlhosting.net',
                             port=3306,
                             user='sql7288305',
                             password='rEGuleh6A7',
                             db='sql7288305',
                             charset='latin1',
                             cursorclass=pymysql.cursors.DictCursor)

def getRecipeByMeal(USER_ID, INTOLERANCE, DIET):
    query = input("Search for meal")
    if (DIET == "regular"):

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
    if Results == []:
        print("No result found or invalid input, try again")
        getRecipeByMeal(1, "", "no")
    else:
        names = list()
        i = 0
        while i < len(Results):
            names.append(Results[i]['title'])
            i += 1
        #print(names)
        Ingredients_list = list()

        j = 0
        while j < len(Results):
            INGREDIENTS1 = getRecipeIngedients(str(Results[j]['id']))
            Ingredients_list.append(INGREDIENTS1)
            j += 1

        number = list(range(1, (len(Results) + 1), 1))

        k = 0
        while (k < (len(Results))):
            summary = list()
            print("https://spoonacular.com/recipeImages/"+str(Results[k]['id'])+"-312x231.jpg")
            summary.extend((number[k], names[k], Ingredients_list[k]))
            print(summary)
            k += 1
        Recipe1 = int(input("Which of the dishes do you wanna choose? (number 1- " + str(len(Results)) + ")"))
        global Recipe_ID
        Recipe_ID = str(Results[Recipe1 - 1]['id'])
        global INGREDIENTS
        INGREDIENTS = Ingredients_list[Recipe1 - 1]
        INGREDIENTS = INGREDIENTS[1:-1]
        INGREDIENTS = INGREDIENTS.replace("\'", " ")
        INGREDIENTS = INGREDIENTS.replace("', '", ",")
        INGREDIENTS = INGREDIENTS.split(",")
        #print(INGREDIENTS)
        #print(type(INGREDIENTS))
        global RECIPE_NAME
        RECIPE_NAME = str(names[Recipe1 - 1])
        global CALORIES
        i = 0
        calories = list()
        while (i < (len(INGREDIENTS))):
            #print(INGREDIENTS[i])
            calories_1 = food_nutrition(INGREDIENTS[i])
            calories.append(calories_1)
            i += 1
        CALORIES = int(sum(calories))
        print("Calories:"+str(CALORIES))
        global RECIPE
        RECIPE = getRecipeInformation(Recipe_ID)

        test_fav = input("Do you wanna save the recipe in your favourites? yes/no")
        if (test_fav == "yes"):
            dbNewFav(connection, Recipe_ID, RECIPE_NAME, RECIPE, USER_ID, INGREDIENTS,CALORIES)
            pass
        else:
            choice2 = input("Do you want to search for another recipe? yes/no")
            if (choice2 == "yes"):
                getRecipeByMeal(USER_ID,INTOLERANCE,DIET)
            else:
                pass


def getRecipeByIngredients(USER_ID):
    #get recipe by ingredients
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
    #print(INGREDIENTS)
    global RECIPE_NAME
    RECIPE_NAME = str(names[Recipe1-1])
    global CALORIES
    i = 0
    calories = list()
    while (i < (len(INGREDIENTS))):
        calories_1 = food_nutrition(INGREDIENTS[i])
        calories.append((int(calories_1)))
        i += 1
    CALORIES = int(sum(calories))
    print("Calories:"+str(CALORIES))
    global RECIPE
    RECIPE = getRecipeInformation(Recipe_ID)

    i = 0
    ing = list()
    while (i < (len(INGREDIENTS))):
        ing.append(FoodNutritionsDao.checkFoodInApi(INGREDIENTS[i]))
        i += 1
    print(ing)

    test_fav = input("Do you wanna save the recipe in your favourites? yes/no")
    if (test_fav == "yes"):
        dbNewFav(connection, Recipe_ID, RECIPE_NAME, RECIPE, USER_ID, INGREDIENTS, CALORIES)
    else:
        choice2 = input("Do you want to search for another recipe? yes/no")
        if (choice2 == "yes"):
            getRecipeByIngredients(USER_ID)
        else:
            pass

def getRecipeIngedients(Recipe_ID):
    #api to get recipe ingredients
    try:
        response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+Recipe_ID+"/ingredientWidget.json",
                               headers={
                                   "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                                   "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
                               }
                               )
        #pprint.pprint(response.json())
        Recipe2 = response.json()
        i = 0
        ingredients1 = list()
        while i < (len(Recipe2['ingredients'])-1):
            ingredient = str(Recipe2['ingredients'][i]['amount']['metric']['value']) + " " + Recipe2['ingredients'][i]['amount']['metric']['unit'] + " " + Recipe2['ingredients'][i]['name']
            ingredients1.append(ingredient)
            i += 1
        #print(ingredients1)
        return str(ingredients1)
    except Exception:
        #print ("Sorry we couldn't find the Ingredients")
        return ("No ingredients found")

def getRecipeInformation(Recipe_ID):
    #api to get recipe for the choosen meal
    try:
        response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+Recipe_ID+"/information",
                               headers={
                                   "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                                   "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
                               }
                               )
        #pprint.pprint(response.json())
        Recipe2 = response.json()
        pprint.pprint(Recipe2['instructions'])
        return str(Recipe2['instructions'])
    except Exception:
        #print("Sorry we couldn't find the recipe")
        return "Sorry we couldn't find the recipe"  #change later


def dbNewFav(connection, Recipe_ID, RECIPE_NAME, RECIPE,USER_ID, INGREDIENTS, CALORIES):
    #adds new entry to the FAV_RECIPE table
    #add test Fav_Recipe DB entry exist User_ID and Reciep_ID
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
            print("insert successful") #what to do if Recipe_ID already exists

    finally:
        cursor.close()



if __name__ == '__main__':
    pass
    #dbLogin()
    #getRecipeIngedients("849492")
    #connection.close()
    #getRecipeInformation("849492")
    #getRecipeByMeal(1,"tomato","no")
    #getRecipeByIngredients(1)
    #food_nutrition("i ate 2 eggs, ten strawberries, and 10 french toast")
