from dbFunctions import *
from datetime import date
import pymysql

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
            info = cursor.fetchone()
            return info
    finally:
        cursor.close()


if __name__ == "__main__":
    pass