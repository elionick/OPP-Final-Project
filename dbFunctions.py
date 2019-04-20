import pymysql
import datetime

connection = pymysql.connect(host='sql7.freemysqlhosting.net',
                             port=3306,
                             user='sql7288305',
                             password='rEGuleh6A7',
                             db='sql7288305',
                             charset='latin1',
                             cursorclass=pymysql.cursors.DictCursor)


def addnewMigrosPrice(product, productEntries):

    for i in range(len(productEntries)):
        productEntries[i] = productEntries[i].split(",")

    product = product.replace(" ","_")

    try:
        with connection.cursor() as cursor:
            for i in range(len(productEntries)):

                sql = "INSERT INTO "+product +" (brand, product, price, date) VALUES (%s, %s, %s, %s)"
                print(sql)
                cursor.execute(sql, (productEntries[i][0], productEntries[i][1],
                                    productEntries[i][2], datetime.date.today()))

    finally:
        connection.commit()
        connection.close()