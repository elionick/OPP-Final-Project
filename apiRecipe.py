from recipeDao import *
from classPriceCatcher import *
from checkFunctions import *
from foodLogDao import *

class apiRecipe:
    def __init__(self, USER_ID, INTOLERANCE, DIET):
        self.headers = {"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com", "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"}
        self.INTOLERANCE = INTOLERANCE
        self.DIET = DIET
        self.USER_ID = USER_ID
        self.Recipe_ID = int()
        self.INGREDIENTS = []
        self.CALORIES = []
        self.RECIPE = []
        self.PRICE = int()

    def getRecipeByMeal(self):
        query = input("Search for meal")
        if (self.DIET == "regular"):

            r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?intolerances="+self.INTOLERANCE+"&number=20&offset=0&type=main+course&query="+query+"",
            headers = self.headers
            )
        else:
            r = requests.get(
                "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search?diet="+self.DIET+"&intolerances="+self.INTOLERANCE+"&number=20&offset=0&type=main+course&query="+query+"",
                headers = self.headers
                )
        Result = r.json()
        Results = Result['results']
        #pprint.pprint(Results)
        if Results == []:
            print("No result found or invalid input, try again")
            self.getRecipeByMeal()
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
                INGREDIENTS1 = apiRecipe.getRecipeIngedients(str(Results[j]['id']))
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
            Recipe1 = input("Which of the dishes do you wanna choose? (number 1- " + str(len(Results)) + ")")
            while checkStringIsInt(Recipe1) == False:
                Recipe1 = input("Which of the dishes do you wanna choose? (number 1- " + str(len(Results)) + ")")
            Recipe1 = int(Recipe1)
            while Recipe1 not in range(1, (len(Results) + 1), 1):
                Recipe1 = int(input("Please enter a number between 1- " + str(len(Results))))
            self.Recipe_ID = str(Results[Recipe1 - 1]['id'])

            INGREDIENTS2 = Ingredients_list[Recipe1 - 1]
            INGREDIENTS2 = INGREDIENTS2[1:-1]
            INGREDIENTS2 = INGREDIENTS2.replace("\'", " ")
            INGREDIENTS2 = INGREDIENTS2.replace("', '", ",")
            INGREDIENTS2 = INGREDIENTS2.split(",")
            self.INGREDIENTS = INGREDIENTS2
            print(self.INGREDIENTS)
            #print(type(INGREDIENTS))

            self.RECIPE_NAME = str(names[Recipe1 - 1])

            i = 0
            calories = list()
            while (i < (len(self.INGREDIENTS))):
                calories_1 = apiFoodNutritions.getCalories(self.INGREDIENTS[i])
                calories.append((int(calories_1)))
                i += 1
            self.CALORIES = int(sum(calories))
            print("Calories:" + str(self.CALORIES))

            self.RECIPE = apiRecipe.getRecipeInformation(self.Recipe_ID)

            price = list()
            ingredients = self.INGREDIENTS
            # Create a new instance of the class, the input will be the ingredients list
            test = priceRetriever(ingredients)

            # Checks which of the ingredients is a food item with the API
            test.findIngredients()
            #print(test.finalIngredients)

            # Translate these ingredients
            test.translateIngredients()
            #print(test.finalIngredients)

            # Get the cheapest product - The result will be in the instance variable "self.IngredientPrices"
            test.getCoopPrices()
            #print(test.IngredientPrices)
            i = 0
            while i < len(self.INGREDIENTS):
                test1 = test.IngredientPrices[i]
                test1 = test1.split(",")
                #print(test1[2])
                price.append(float(test1[2]))
                i += 1
            self.PRICE = sum(price)
            print(self.PRICE)

            food_log = input("Do you wanna add the meal to your food log? yes/no")
            while food_log not in {"yes", "no"}:
                food_log = input("Please enter yes or no: ")
            if food_log == "yes":
                foodLogDao.setMeal(self.RECIPE_NAME, self.CALORIES, self.USER_ID)
            else:
                pass

            test_fav = input("Do you wanna save the recipe in your favourites? yes/no")
            while test_fav not in {"yes", "no"}:
                test_fav = input("Please enter yes or no: ")
            if (test_fav == "yes"):
                if checkRecipeExist(self.USER_ID, self.Recipe_ID) == True:
                    print("Recipe already saved as favourite. Check your favourites")
                    pass
                else:
                    dbNewFavRecipe(self.Recipe_ID, self.RECIPE_NAME, self.RECIPE, self.USER_ID, str(self.INGREDIENTS), self.CALORIES, self.PRICE)
                    pass
            else:
                choice2 = input("Do you want to search for another recipe? yes/no")
                while choice2 not in {"yes", "no"}:
                    choice2 = input("Please enter yes or no: ")
                if (choice2 == "yes"):
                    self.getRecipeByMeal()
                else:
                    pass

    def getRecipeByIngredients(self):
        #get recipe by ingredients
        query = input("Insert the ingredients")

        r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=20&ranking=1&ignorePantry=false&ingredients="+query+"",
                headers= self.headers
                )
        Results = r.json()
        names = list()
        if Results == []:
            print("No result found or invalid input, try again")
            self.getRecipeByIngredients()
        else:
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
            Recipe1 = input("Which of the dishes do you want to choose? (number 1- "+str(len(Results))+")")
            while checkStringIsInt(Recipe1) == False:
                Recipe1 = input("Which of the dishes do you wanna choose? (number 1- " + str(len(Results)) + ")")
            Recipe1 = int(Recipe1)
            while Recipe1 not in range(1, (len(Results) + 1), 1):
                Recipe1 = int(input("Please enter a number between 1- " + str(len(Results))))
            self.Recipe_ID = str(Results[Recipe1-1]['id'])

            self.INGREDIENTS = Ingredients_list[Recipe1-1]
            print(self.INGREDIENTS)

            self.RECIPE_NAME = str(names[Recipe1-1])

            i = 0
            calories = list()
            while (i < (len(self.INGREDIENTS))):
                calories_1 = apiFoodNutritions.getCalories(self.INGREDIENTS[i])
                calories.append((int(calories_1)))
                i += 1
            self.CALORIES = int(sum(calories))
            print("Calories:"+str(self.CALORIES))

            self.RECIPE = apiRecipe.getRecipeInformation(self.Recipe_ID)

            price = list()
            # Create a new instance of the class, the input will be the ingredients list
            test = priceRetriever(self.INGREDIENTS)

            # Checks which of the ingredients is a food item with the API
            test.findIngredients()
            #print(test.finalIngredients)

            # Translate these ingredients
            test.translateIngredients()
            #print(test.finalIngredients)

            # Get the cheapest product - The result will be in the instance variable "self.IngredientPrices"
            test.getCoopPrices()
            #print(test.IngredientPrices)
            i = 0
            while i < len(self.INGREDIENTS):
                test1 = test.IngredientPrices[i]
                test1 = test1.split(",")
                #print(test1[2])
                price.append(float(test1[2]))
                i += 1
            self.INGREDIENTSPRICE = sum(price)
            print(self.INGREDIENTSPRICE)

            food_log = input("Do you wanna add the meal to your food log? yes/no")
            while food_log not in {"yes", "no"}:
                food_log = input("Please enter yes or no: ")
            if food_log == "yes":
                foodLogDao.setMeal(self.RECIPE_NAME, self.CALORIES, self.USER_ID)
            else:
                pass

            test_fav = input("Do you wanna save the recipe in your favourites? yes/no")
            while test_fav not in {"yes", "no"}:
                test_fav = input("Please enter yes or no: ")
            if (test_fav == "yes"):
                if checkRecipeExist(self.USER_ID,self.Recipe_ID) == True:
                    print("Recipe already saved as favourite. Check your favourites")
                    pass
                else:
                    dbNewFavRecipe(int(self.Recipe_ID), str(self.RECIPE_NAME), self.RECIPE, int(self.USER_ID), str(self.INGREDIENTS), self.CALORIES, self.PRICE)
                    input("Press enter to go back to the recipe menu")
                    pass
            else:
                choice2 = input("Do you want to search for another recipe? yes/no")
                while choice2 not in {"yes", "no"}:
                    choice2 = input("Please enter yes or no: ")
                if (choice2 == "yes"):
                    self.getRecipeByIngredients()
                else:
                    pass
    @staticmethod
    def getRecipeIngedients(Recipe_ID):
        #api to get recipe ingredients
        try:
            response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+Recipe_ID+"/ingredientWidget.json",
                                   headers= {"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com", "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"}
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

    def getRecipeInformation(self):
        #api to get recipe for the choosen meal
        try:
            response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+self.Recipe_ID+"/information",
                                   headers = self.headers
                                   )
            #pprint.pprint(response.json())
            Recipe2 = response.json()
            pprint.pprint(Recipe2['instructions'])
            return str(Recipe2['instructions'])
        except Exception:
            return "Sorry we couldn't find the recipe"



if __name__ == '__main__':
    #pass
    test1 = apiRecipe(1,"tomato","regular")
    test1.getRecipeByMeal()
    # getRecipeByMeal

