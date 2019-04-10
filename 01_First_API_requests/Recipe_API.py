import requests
import pprint

query = input("search for meal")
diet = input("are you doing a diet?")

def getRecipeByIngredients():
    if diet == False:

        r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?number=10&offset=0&type=main+course&query="+query+"",
        headers={
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
        }
        )
    else:
        r = requests.get(
            "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?diet = "+diet+"number=10&offset=0&type=main+course&query=" + query + "",
            headers={
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
            }
            )
    pprint.pprint(r.json())

def getRecipeInformation(Recipe_ID):
    response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+Recipe_ID+"/information",
                           headers={
                               "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                               "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
                           }
                           )
    pprint.pprint(response.json())

if __name__ == "__main__":
  #  getRecipeByIngredients()
    getRecipeInformation("521885")