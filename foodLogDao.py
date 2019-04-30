from dbFunctions import *
import datetime
class foodLogDao:
    @staticmethod
    def setMeal(meal_name, calories, user_id):
        try:
            with connection.cursor() as cursor:
                sql = "insert into FOOD_LOG (FK_USER_ID, CALORIES, MEAL_NAME, DATE) values (%s, %s, %s, %s)"
                cursor.execute(sql, (user_id, calories, meal_name, datetime.datetime.today().date()))
                connection.commit()
        finally:
            cursor.close()
    @staticmethod
    def getTodaysCaloricIntake(user_id):
        try:
            with connection.cursor() as cursor:
                sql = "select CALORIES from FOOD_LOG where FK_USER_ID = %s and DATE = %s"
                cursor.execute(sql, (user_id, datetime.date.today()))
                info = cursor.fetchall()
                return sum([v['CALORIES'] for v in info])
        finally:
            cursor.close()
if __name__ == "__main__":
    pass
    