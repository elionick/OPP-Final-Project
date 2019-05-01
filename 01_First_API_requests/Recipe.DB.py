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


def getRecipeByMeal():
    query = input("search for meal")
    if (DIET == "no"):

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
    Results = r.json()
    if (int(Results['totalResults'])== 0):
        print("no result found")
        recipe = input("Do you want to search for another recipe?")
        if (recipe == "yes"):
            getRecipeByIngredients()
        else: exit()
    else:
        getRecipeDetails(Results)

def getRecipeByIngredients():
    query = input("search for ingredients")

    r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=5&ranking=1&ignorePantry=false&ingredients="+query+"",
            headers={
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
            }
            )
    Results = r.json()
    getRecipeDetails(Results)

def getRecipeDetails(Results):
        #Recipe = str(Results['results'])
        #Recipe = Recipe[1:-1]
        pprint.pprint(Results)
        Recipe1 =input("If you want to see the recipe of one of the dishes enter the ID, otherwise enter no")
        if (Recipe1 == "no"):
            choice = input("Do you want to search for another recipe? yes/no")
            if (choice == "no"):
                exit()
            else: getRecipeByIngredients()
        else:
            global Recipe_ID
            Recipe_ID = str(Recipe1)
            print("successful")
            getRecipeInformation(Recipe_ID)
            getRecipeIngedients(Recipe_ID)
            Recipe_ID = int(Recipe_ID)
            test_fav = input("Do you wanna save the recipe in your favourites? yes/no")
            if (test_fav == "yes"):
                dbNewFav(connection,Recipe_ID,RECIPE_NAME,RECIPE,USER_ID,INGREDIENTS)
            else:
                choice2 = input("Do you want to search for another recipe? yes/no")
                if (choice2 == "no"):
                    exit()
                else: getRecipeByIngredients()




def getRecipeInformation(Recipe_ID):
    response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+Recipe_ID+"/information",
                           headers={
                               "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                               "X-RapidAPI-Key": "8ad4046d49msha3912eb864b6baep193b5bjsne4b65b911209"
                           }
                           )
    pprint.pprint(response.json())
    Recipe2 = response.json()
    if (Recipe2 == "{'code': 404,'message': 'A recipe with the id "+Recipe_ID+" does not exist.','status': 'failure'}"):
        print("couldn't find the recipe")
        choice3 = input("Do you want to search for another recipe? yes/no")
        if (choice3 == "no"):
            exit()
        else:
            getRecipeByIngredients()
    else:
        RECIPE_NAME1 = str(Recipe2['title'])
        global RECIPE_NAME
        RECIPE_NAME = RECIPE_NAME1[0:254]
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




def dbInfoUser(connection, LOGIN_NAME):
    try:
        with connection.cursor() as cursor:
            sql = "select USER_ID,LOGIN_NAME,FIRST_NAME,LAST_NAME,cast(BIRTHDATE as char) AS BIRTHDAY ,HEIGHT,WEIGHT,DIET,INTOLERANCE FROM USER WHERE LOGIN_NAME = %s"
            cursor.execute(sql, LOGIN_NAME)
            output = cursor.fetchone()
            global USER_ID
            USER_ID = output['USER_ID']
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

def dbCheckPassword(connection, LOGIN_NAME):
    try:
        with connection.cursor() as cursor:
            PASSWORD_HASH = input('PASSWORD or exit with q')
            if (PASSWORD_HASH == "q"):
                exit()
            else:
                sql = "select  LOGIN_NAME, COUNT(USER_ID) FROM USER WHERE LOGIN_NAME = %s AND cast(aes_decrypt(PASSWORD_HASH, 'key123') as char(100)) = %s"
                cursor.execute(sql, (LOGIN_NAME, PASSWORD_HASH))
                info = cursor.fetchone()
                COUNT = int(info['COUNT(USER_ID)'])
                if COUNT > 0:
                    print("Password correct")
                else:
                    print("wrong Password")
                    LOGIN_NAME = input('LOGIN_NAME')
                    dbCheckPassword(connection, LOGIN_NAME)


    finally:
        cursor.close()

def dbCheckLoginName(connection,LOGIN_NAME):
    try:
        with connection.cursor() as cursor:

            sql = "select  COUNT(USER_ID),LOGIN_NAME FROM USER WHERE LOGIN_NAME = %s"
            cursor.execute(sql, LOGIN_NAME)
            info = cursor.fetchone()
            COUNT = int(info['COUNT(USER_ID)'])
            if COUNT > 0:
                print("Login name already exists")
                dbNewUser(connection)
            else:
                True

    finally:
        cursor.close()

def dbNewFav(connection, Recipe_ID, RECIPE_NAME, RECIPE,USER_ID, INGREDIENTS):
    try:
        with connection.cursor() as cursor:
           # CALORIES = input("CALORIES")
            #PRICE = input("PRICE")
            #ALLEGIES = input("ALLEGIES")
            #INTOLERANCE = input("INTOLERANCE")
            sql = "INSERT INTO FAV_RECIPE (RECIPE_ID,RECIPE_NAME,RECIPE,USER_ID, INGREDIENTS)"\
             + "VALUES (%s,%s,%s,%s, %s)"
            cursor.execute(sql, (Recipe_ID,RECIPE_NAME,RECIPE,USER_ID,INGREDIENTS)) #,CALORIES,PRICE,ALLEGIES,INTOLERANCE))
            connection.commit()
            print("insert successful")

    finally:
        cursor.close()

def dbNewUser(connection):
    try:
        with connection.cursor() as cursor:
            global LOGIN_NAME
            LOGIN_NAME = input('LOGIN_NAME')
            dbCheckLoginName(connection,LOGIN_NAME)
            PASSWORD_HASH = input('PASSWORD')
            FIRST_NAME = input('FIRST_NAME')
            LAST_NAME = input('LAST_NAME')
            BIRTHDATE = input('BIRTHDATE (YYYY-mm-dd)')
            HEIGHT = input('HEIGHT')
            WEIGHT = input('WEIGHT')
            ALorINT = input('Are you doing a diet or do you have any allergies or intolerance (yes/no)')
            if (ALorINT == 'no'):
                sql = "INSERT INTO USER (LOGIN_NAME,PASSWORD_HASH,FIRST_NAME,LAST_NAME,BIRTHDATE,HEIGHT,WEIGHT)"\
                 + "VALUES (%s,AES_ENCRYPT(%s,'key123'), %s,%s, %s, %s, %s)"
                cursor.execute(sql, (LOGIN_NAME,PASSWORD_HASH,FIRST_NAME,LAST_NAME,BIRTHDATE,HEIGHT,WEIGHT))
                connection.commit()
            else:
                DIET = input("DIET (no, pescetarian, lacto vegetarian, ovo vegetarian, vegan or vegetarian)")
                INTOLERANCE = input("INTOLERANCE")
                sql = "INSERT INTO USER (LOGIN_NAME,PASSWORD_HASH,FIRST_NAME,LAST_NAME,BIRTHDATE,HEIGHT,WEIGHT,DIET,INTOLERANCE)" \
                    + "VALUES (%s,AES_ENCRYPT(%s,'key123'), %s,%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (LOGIN_NAME, PASSWORD_HASH, FIRST_NAME, LAST_NAME, BIRTHDATE, HEIGHT, WEIGHT,DIET,INTOLERANCE ))
                connection.commit()

                print("insert successful")
    finally:
            cursor.close()

def dbGetUserID(connection, LOGIN_NAME):
    try:
        with connection.cursor() as cursor:
            sql = "select USER_ID,LOGIN_NAME,FIRST_NAME,LAST_NAME,cast(BIRTHDATE as char) AS BIRTHDAY ,HEIGHT,WEIGHT FROM USER WHERE LOGIN_NAME = %s"
            cursor.execute(sql, LOGIN_NAME)
            output = cursor.fetchone()
            print(output)
            global USER_ID
            USER_ID = int(output['USER_ID'])
            print("User ID is:")
            print(USER_ID)
    finally:
        cursor.close()

def dbLogin():
    account = input("Do you have an existing account? (yes/no)")
    if (account == "no"):
        dbNewUser(connection)
    if (account == "yes"):
        global LOGIN_NAME
        LOGIN_NAME = input('LOGIN_NAME')
        dbCheckPassword(connection, LOGIN_NAME)
    else:
        print("wrong input. Please select yes or no")
        dbLogin()
    recipe = input("Do you want to search for a recipe? yes/no ")
    dbInfoUser(connection,LOGIN_NAME)
    if (recipe == "yes"):
        recipe3 = input("You you want to input a meal or the ingredients you have at home? meal/ingredients")
        if (recipe3 == "meal"):
            getRecipeByMeal()
        if (recipe3 == "ingredients"):
            getRecipeByIngredients()
    else:
        recipe2 = input("Do you want to exit or search for a recipe? (recipe or q for exit)")
        if (recipe2 == "q"):
            exit()
        if (recipe2 == "recipe"):
            recipe3 = input("You you want to input a meal or the ingredients you have at home? meal/ingredients")
            if (recipe3 == "meal"):
                getRecipeByMeal()
            if (recipe3 == "ingredients"):
                getRecipeByIngredients()
        else:
            print("no valid input")
            exit()


if __name__ == '__main__':

    dbLogin()

    connection.close()
