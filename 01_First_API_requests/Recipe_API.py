import requests
import pprint
import pymysql

LOGIN_NAME = input('LOGIN_NAME')

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Andreas1',
                             db='dbOOP',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

dbLogin()
USER_ID = dbGetUserID(connection, LOGIN_NAME)

query = input("search for meal")
diet = input("are you doing a diet? (Possible values are: pescetarian, lacto vegetarian, ovo vegetarian, vegan, and vegetarian)")
intolerance = input("Do you have any intolerances? A comma-separated list of intolerances.")

def getRecipeByIngredients():
    if (diet == "no"):

        r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?intolerances="+intolerance+"&number=1&offset=0&type=main+course&query="+query+"",
        headers={
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
        }
        )
    else:
        r = requests.get(
            "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?diet="+diet+"&intolerances="+intolerance+"&number=1&offset=0&type=main+course&query="+query+"",
            headers={
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
            }
            )
    pprint.pprint(r.json())
    Results = r.json()
    Recipe = str(Results['results'])
    Recipe = Recipe[1:-1]
    global Recipe_ID
    Recipe_ID = str(Recipe[7:13])
    print(Recipe)
    print(Recipe_ID)
    getRecipeInformation(Recipe_ID)
    getRecipeIngedients(Recipe_ID)
    Recipe_ID = int(Recipe_ID)
    dbNewFav(connection,Recipe_ID,RECIPE_NAME,RECIPE,USER_ID,INGREDIENTS)




def getRecipeInformation(Recipe_ID):
    response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+Recipe_ID+"/information",
                           headers={
                               "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                               "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
                           }
                           )
    pprint.pprint(response.json())
    Recipe2 = response.json()
    global RECIPE_NAME
    RECIPE_NAME = str(Recipe2['title'])
    RECIPE1 = str(Recipe2['instructions'])
    global RECIPE
    RECIPE = RECIPE1[0:254]
def getRecipeIngedients(Recipe_ID):
    response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+Recipe_ID+"/ingredientWidget.json",
                           headers={
                               "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                               "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
                           }
                           )
    pprint.pprint(response.json())
    Recipe2 = response.json()
    INGREDIENTS1 = str(Recipe2['ingredients'])
    global INGREDIENTS
    INGREDIENTS = INGREDIENTS1[0:254]
    #RECIPE = str(Recipe2['instructions'])

if __name__ == "__main__":

    getRecipeByIngredients()
    INGREDIENTS
    #getRecipeInformation("648399")
    #getRecipeIngedients('219957')
    #print(Recipe_ID, RECIPE, RECIPE_NAME, INGREDIENTS)

