from dbFunctions import *
class exerciseDao:
    def createExercise(self, name, duration, calories, workout_id):
        try:
            with connection.cursor() as cursor:
                sql = "insert into EXERCISES (NAME, DURATION, CALORIES,FK_WORKOUT_ID) values (%s, %s, %s, %s)"
                cursor.execute(sql, (name, duration, calories, workout_id))
                connection.commit()
        finally:
            cursor.close()
    def deleteExercise(self, name):
        try:
            with connection.cursor() as cursor:
                sql = f"delete from EXERCISES where NAME = {name}"
                cursor.execute(sql)
                connection.commit()
        finally:
            cursor.close()
    def getExerciseDic(self, workout_id):
        try:
            with connection.cursor() as cursor:
                sql = "select * FROM EXERCISES WHERE FK_WORKOUT_ID = %s"
                cursor.execute(sql, workout_id)
                info = cursor.fetchall()
        finally:
            cursor.close()
        return info

if __name__ == "__main__":
    pass