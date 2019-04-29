from dbFunctions import *
from datetime import date
import pymysql
import pprint
from dbFunctions import getRecipeList


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



if __name__ == "__main__":
    pass