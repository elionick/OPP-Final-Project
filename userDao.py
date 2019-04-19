from dbFunctions import *

# Unique Username required
def checkUsernameExists(username):
    try:
        with connection.cursor() as cursor:
            sql = "select COUNT(LOGIN_NAME) FROM USER WHERE LOGIN_NAME = %s"
            cursor.execute(sql, username)
            info = cursor.fetchone()
            COUNT = int(info['COUNT(LOGIN_NAME)'])
            if COUNT == 1:
                return True
            else:
                return False

    finally:
        cursor.close()

# Check password for unique username
def checkPasswordValid(username, password):
    try:
        with connection.cursor() as cursor:
            sql = "select COUNT(LOGIN_NAME) FROM USER WHERE LOGIN_NAME = %s and PASSWORD_HASH = cast(aes_encrypt(%s, 'key123') as char(100))"
            cursor.execute(sql, (username, password))
            info = cursor.fetchone()
            COUNT = int(info['COUNT(LOGIN_NAME)'])
            if COUNT == 1:
                return True
            else:
                return False
    finally:
        cursor.close()

# Set a user field
def setValueForUserInField(username, field_name, value, is_password = False):
    user_id = getUserID(username)
    if is_password == False:
        try:
            with connection.cursor() as cursor:
                sql = "update USER set "+ field_name + " = %s where USER_ID = %s"
                cursor.execute(sql, (value, user_id))
                connection.commit()
        finally:
            cursor.close()
    elif is_password == True:
        try:
            with connection.cursor() as cursor:
                sql = "update USER set " + field_name + " = AES_ENCRYPT(%s,'key123') where USER_ID = %s"
                cursor.execute(sql, (value, user_id))
                connection.commit()
        finally:
            cursor.close()

def getUserID(username):
    try:
        with connection.cursor() as cursor:
            sql = "select USER_ID FROM USER WHERE LOGIN_NAME = %s"
            cursor.execute(sql, username)
            info = cursor.fetchone()
    finally:
        cursor.close()
    return int(info['USER_ID'])

# Create a new user
def createUser(username, password = None, first_name = None, middle_name = None, last_name = None,
        height = None, weight = None, birthdate = None, diet = None, intolerance = None):
    try:
        with connection.cursor() as cursor:
            sql = "insert into USER (LOGIN_NAME) value (%s)"
            cursor.execute(sql, username)
            connection.commit()
    finally:
        cursor.close()
    if password != None:
        setValueForUserInField(username, "PASSWORD_HASH", password, is_password = True)
    inputs = [first_name, middle_name, last_name, height, weight, birthdate, diet, intolerance]
    sql_field_names = ["FIRST_NAME", "MIDDLE_NAME", "LAST_NAME", "HEIGHT", "WEIGHT", "BIRTHDATE", "DIET", "INTOLERANCE"]
    for index, element in enumerate(inputs):
        if element != None:
            setValueForUserInField(username, sql_field_names[index], inputs[index])

if __name__ == "__main__":
    createUser("test32", first_name= "Edward", password="eddie")
    print(checkPasswordValid("test32", "eddie"))