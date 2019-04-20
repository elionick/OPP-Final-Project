import pymysql
import datetime


connection = pymysql.connect(host='sql7.freemysqlhosting.net',
                             port=3306,
                             user='sql7288305',
                             password='rEGuleh6A7',
                             db='sql7288305',
                             charset='latin1',
                             cursorclass=pymysql.cursors.DictCursor)


def createTable():
    try:
        with connection.cursor() as cursor:
            sql = "CREATE TABLE Knoblauch (brand VARCHAR(255), product VARCHAR(255), price TEXT(50), date TEXT (50))"
            cursor.execute(sql)

    finally:
        cursor.close()


# def addnewMigrosPrice(productEntries):
#
#     for i in range(len(productEntries)):
#         productEntries[i] = productEntries[i].split(",")
#
#     try:
#         with connection.cursor() as cursor:
#             for i in range(len(productEntries)):
#
#                 sql = "INSERT INTO prices (brand, product, price, date) VALUES (%s, %s, %s, %s)"
#
#                 cursor.execute(sql, (productEntries[i][0], productEntries[i][1],
#                                      productEntries[i][2], datetime.date.today()))
#
#     finally:
#         connection.commit()
#         connection.close()

createTable()
