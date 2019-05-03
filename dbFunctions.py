import pymysql
import datetime

connection = pymysql.connect(host='sql7.freemysqlhosting.net',
                             port=3306,
                             user='sql7288305',
                             password='rEGuleh6A7',
                             db='sql7288305',
                             charset='latin1',
                             cursorclass=pymysql.cursors.DictCursor)


def checkTableExist(tablename):

    tablename = tablename.replace(" ", "_")
    tablename = tablename.replace("-", "_")
    tablename = tablename.upper()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name= '" + \
                tablename + "'"
            print(sql)
            cursor.execute(sql)
            if cursor.fetchone()["COUNT(*)"] == 1:
                return True
            else:
                return False
    finally:
        connection.commit()
        cursor.close()


def createNewPriceTable(tablename, column1, column2, column3, column4, column5):

    tablename = tablename.replace(" ", "_")
    tablename = tablename.upper()

    try:
        with connection.cursor() as cursor:
            sql = "CREATE TABLE " + tablename + " (" + column1 + " INT NOT NULL AUTO_INCREMENT, "+column2 + " VARCHAR(255), " + column3\
                  + " VARCHAR(255), " + column4 + " TEXT(50), " + column5 + \
                " DATE NOT NULL, PRIMARY KEY (" + column1 + "))"
            print(sql)
            cursor.execute(sql)

    finally:
        connection.commit()
        cursor.close()


