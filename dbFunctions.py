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


def addNewPrice(product, productEntries):

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


def dbNewFavRecipe(Recipe_ID, RECIPE_NAME, RECIPE,USER_ID, INGREDIENTS, CALORIES):
    #adds new entry to the FAV_RECIPE table
    #add test Fav_Recipe DB entry exist User_ID and Reciep_ID
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO FAV_RECIPE (RECIPE_ID,RECIPE_NAME,RECIPE,USER_ID, INGREDIENTS, CALORIES)"\
             + "VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (Recipe_ID,RECIPE_NAME,RECIPE,USER_ID,INGREDIENTS,CALORIES))
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


def checkRecipeExist(USER_ID,Recipe_ID):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) FROM FAV_RECIPE WHERE USER_ID = %s AND RECIPE_ID = %s"
            cursor.execute(sql, (USER_ID,Recipe_ID))
            if cursor.fetchone()["COUNT(*)"] == 1:
                return True
            else:
                return False

    finally:
        cursor.close()

