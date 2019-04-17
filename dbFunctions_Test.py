import pymysql
import datetime

# def createTable():
#     try:
#         with connection.cursor() as cursor:
#             sql = "CREATE TABLE prices (brand VARCHAR(255), product VARCHAR(255), price TEXT(50), date TEXT (50))"
#             cursor.execute(sql)
#
#     finally:
#         cursor.close()

#


def addnewMigrosPrice(productEntries):

    for i in range(len(productEntries)):
        productEntries[i] = productEntries[i].split(",")

    connection = pymysql.connect(host='localhost', user='oop',
                                 password='password123', db="project_db", cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            for i in range(len(productEntries)):

                sql = "INSERT INTO prices (brand, product, price, date) VALUES (%s, %s, %s, %s)"

                cursor.execute(sql, (productEntries[i][0], productEntries[i][1],
                                     productEntries[i][2], datetime.date.today()))

    finally:
        connection.commit()
        connection.close()
