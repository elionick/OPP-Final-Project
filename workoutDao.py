from dbFunctions import *

class workoutDao:
    def setWorkout(self, starttime, weekday, user_id):
        try:
            with connection.cursor() as cursor:
                sql = "insert into WORKOUTS (TIME, WEEKDAY, FK_USER_ID) values (%s, %s, %s)"
                cursor.execute(sql, (starttime, weekday, user_id))
                connection.commit()
        finally:
            cursor.close()
    def getWorkoutId(self, starttime, weekday, user_id):
        try:
            with connection.cursor() as cursor:
                sql = "select WORKOUT_ID FROM WORKOUTS WHERE FK_USER_ID = %s and TIME = %s and WEEKDAY = %s"
                cursor.execute(sql, (user_id, starttime, weekday))
                info = cursor.fetchone()
        finally:
            cursor.close()
        return int(info['WORKOUT_ID'])


if __name__ == "__main__":
    workoutDao.setWorkout(workoutDao, "12:30", "MON", 24)
    print(workoutDao.getWorkoutId(workoutDao, "12:30", "MON", 24))