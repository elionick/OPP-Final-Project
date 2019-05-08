from dbFunctions import *
from datetime import date
import pprint
from foodLogDao import *


def chooseRecipe(USER_ID):
    info = getRecipeList(USER_ID)
    if info == ():
        print("You don't have any favourites")
        pass
    else:
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
        except Exception:
            print("Index not found")
        food_log = input("Do you wanna add the meal to your food log? yes/no")
        while food_log not in {"yes", "no"}:
            food_log = input("Please enter yes or no: ")
        if food_log == "yes":
            foodLogDao.setMeal(info[(int(choice)-1)]['RECIPE_NAME'],info[(int(choice)-1)]['CALORIES'],USER_ID)
        else:
            pass
        pass

def deleteRecipe(USER_ID):
    info = getRecipeList(USER_ID)
    if info == ():
        print("You don't have any favourites")
        pass
    else:
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
        choice = int(input("Which recipe do you wanna delete?"))
        RECIPE_ID = int(info[choice - 1]['RECIPE_ID'])
        try:
            with connection.cursor() as cursor:
                sql = "delete FROM sql7288305.FAV_RECIPE where USER_ID = %s and RECIPE_ID = %s"
                cursor.execute(sql, (USER_ID, RECIPE_ID))
                connection.commit()

        except Exception:
            print("Index not found")

        finally:
            cursor.close()

        pass

def dbNewFavRecipe(Recipe_ID, RECIPE_NAME, RECIPE, USER_ID, INGREDIENTS, CALORIES, PRICE):
    # adds new entry to the FAV_RECIPE table
    # add test Fav_Recipe DB entry exist User_ID and Reciep_ID
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO FAV_RECIPE (RECIPE_ID,RECIPE_NAME,RECIPE,USER_ID, INGREDIENTS, CALORIES, PRICE)"\
                + "VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (Recipe_ID, RECIPE_NAME, RECIPE, USER_ID, INGREDIENTS, CALORIES, PRICE))
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
    deleteRecipe(1)
#1088227