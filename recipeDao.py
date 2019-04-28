from dbFunctions import *
from datetime import date
import pymysql
import pprint

connection = pymysql.connect(host='sql7.freemysqlhosting.net',
                             port=3306,
                             user='sql7288305',
                             password='rEGuleh6A7',
                             db='sql7288305',
                             charset='latin1',
                             cursorclass=pymysql.cursors.DictCursor)


def getRecipeList(USER_ID):
    try:
        with connection.cursor() as cursor:
            sql = "select * FROM FAV_RECIPE WHERE USER_ID = %s"
            cursor.execute(sql, USER_ID)
            info = cursor.fetchall()
            return info
    finally:
        cursor.close()

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