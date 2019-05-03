from dbFunctions import *

def addNewPrice(product, productEntries):

    try:
        for i in range(len(productEntries)):
            productEntries[i] = productEntries[i].split(",")

    product = product.replace(" ", "_")
    product = product.upper()

    try:
        with connection.cursor() as cursor:
            for i in range(len(productEntries)):
                sql = "INSERT INTO "+product + \
                    " (brand, product, price, date) VALUES (%s, %s, %s, %s)"
                print(sql)
                cursor.execute(sql, (productEntries[i][0], productEntries[i][1],
                                     productEntries[i][2], datetime.date.today()))
    finally:
        connection.commit()
        cursor.close()
