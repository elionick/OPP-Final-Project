from dbFunctions import *
from datetime import date
import pymysql
import pprint
from dbFunctions import *


def chooseRecipe(USER_ID):
    info = getRecipeList(USER_ID)
    i = 0
    recipe_name = list()
    while i < len(info):
        recipe_name.append(info[i]['RECIPE_NAME'])
        i += 1
    number = list(range(1, (len(info)+1), 1))
    i = 0
    while i < (len(info)):
        summary = list()
        summary.extend((number[i], recipe_name[i]))
        print(summary)
        i += 1
    choice = input("Which recipe do you wanna check?")
    try:
        pprint.pprint(info[(int(choice)-1)])
    except Exception: print("Index not found")
    pass

def dbNewFavRecipe(Recipe_ID, RECIPE_NAME, RECIPE, USER_ID, INGREDIENTS, CALORIES):
    # adds new entry to the FAV_RECIPE table
    # add test Fav_Recipe DB entry exist User_ID and Reciep_ID
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO FAV_RECIPE (RECIPE_ID,RECIPE_NAME,RECIPE,USER_ID, INGREDIENTS, CALORIES)"\
                + "VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (Recipe_ID, RECIPE_NAME, RECIPE, USER_ID, INGREDIENTS, CALORIES))
            connection.commit()
            print("insert successful")

    finally:
        cursor.close()


def getRecipeList(USER_ID):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM FAV_RECIPE WHERE USER_ID = %s"
            cursor.execute(sql, USER_ID)
            info = cursor.fetchall()
            return info
    finally:
        cursor.close()


def checkRecipeExist(USER_ID, Recipe_ID):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) FROM FAV_RECIPE WHERE USER_ID = %s AND RECIPE_ID = %s"
            cursor.execute(sql, (USER_ID, Recipe_ID))
            if cursor.fetchone()["COUNT(*)"] == 1:
                return True
            else:
                return False

    finally:
        cursor.close()

if __name__ == "__main__":
    pass