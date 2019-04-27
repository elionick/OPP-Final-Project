from dbFunctions import *
class userDao:
    @staticmethod
    # Get user attributes from database as list
    def getUserAttributesAsList(username):
        user_id = userDao.getUserID(username)
        try:
            with connection.cursor() as cursor:
                sql = "select FIRST_NAME, MIDDLE_NAME, LAST_NAME, GENDER, HEIGHT, WEIGHT, E_MAIL, BIRTHDATE, DIET, INTOLERANCE, LOGIN_NAME, PASSWORD_HASH FROM USER WHERE USER_ID = %s"
                cursor.execute(sql, user_id)
                info = cursor.fetchone()
                retv = [v for v in info.values()]
                return retv
        finally:
            cursor.close()
    
    @staticmethod
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
    @staticmethod
    # Check password for unique username
    def checkValidPassword(password, username):
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
    @staticmethod
    # Set a user field
    def setValueForUserInField(user_id, field_name, value, is_password = False):
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
    @staticmethod
    # Set a user field
    def getValueOfUserInField(user_id, field_name, is_password = False):
        if is_password == False:
            try:
                with connection.cursor() as cursor:
                    sql = "SELECT " + field_name + " from USER where USER_ID = " + str(user_id)
                    cursor.execute(sql)
                    info = cursor.fetchone()
                    return list(info.values())[0]
            finally:
                cursor.close()
        elif is_password == True:
            try:
                with connection.cursor() as cursor:
                    sql = "SELECT AES_DECRYPT(" + field_name + ",'key123') from USER where USER_ID = " + str(user_id)
                    cursor.execute(sql)
                    info = cursor.fetchone()
                    return list(info.values())[0]
            finally:
                cursor.close()
    @staticmethod
    def getUserID(username):
        try:
            with connection.cursor() as cursor:
                sql = "select USER_ID FROM USER WHERE LOGIN_NAME = %s"
                cursor.execute(sql, username)
                info = cursor.fetchone()
        finally:
            cursor.close()
        return int(info['USER_ID'])
    
    @staticmethod
    # Create a new user 
    def createUserFromList(first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, diet, intolerances, username, password):
        try:
            with connection.cursor() as cursor:
                sql = "insert into USER (LOGIN_NAME) value (%s)"
                cursor.execute(sql, username)
                connection.commit()
        finally:
            cursor.close()
        user_id = userDao.getUserID(username)
        if password != None:
            userDao.setValueForUserInField(user_id, "PASSWORD_HASH", password, is_password = True)
        inputs = [first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, diet, intolerances]
        sql_field_names = ["FIRST_NAME", "MIDDLE_NAME", "LAST_NAME", "GENDER", "HEIGHT", "WEIGHT", "E_MAIL", "BIRTHDATE", "DIET", "INTOLERANCE"]
        for index, element in enumerate(inputs):
            if element != None:
                userDao.setValueForUserInField(user_id, sql_field_names[index], inputs[index])

if __name__ == "__main__":
    pass
    