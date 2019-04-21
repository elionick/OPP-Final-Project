from dbFunctions import *

class workoutDao:
    def initWorkout(self, starttime, weekday, user_id):
        try:
            with connection.cursor() as cursor:
                sql = "insert into WORKOUTS (TIME, WEEKDAY, FK_USER_ID) values (%s, %s, %s)"
                cursor.execute(sql, (starttime, weekday, user_id))
                connection.commit()
        finally:
            cursor.close()


if __name__ == "__main__":
    pass