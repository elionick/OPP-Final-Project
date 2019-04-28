from dbFunctions import *

class workoutDao():
    def __init__(self, user_id, start_time, week_day, from_database = False):
        self.userID = user_id
        self.startTime = start_time
        self.weekday = week_day
        if from_database == False:
            self.setWorkout()
        

    def setWorkout(self):
        try:
            with connection.cursor() as cursor:
                sql = "insert into WORKOUTS (TIME, WEEKDAY, FK_USER_ID) values (%s, %s, %s)"
                cursor.execute(sql, (self.startTime, self.weekday, self.userID))
                connection.commit()
        finally:
            cursor.close()    
    def getWorkoutId(self):
        try:
            with connection.cursor() as cursor:
                sql = "select WORKOUT_ID FROM WORKOUTS WHERE FK_USER_ID = %s and TIME = %s and WEEKDAY = %s"
                cursor.execute(sql, (self.userID, self.startTime, self.weekday))
                info = cursor.fetchone()
        finally:
            cursor.close()
        return int(info['WORKOUT_ID'])
    
    def deleteWorkout(self):
        try:
            with connection.cursor() as cursor:
                sql = "delete from EXERCISES where FK_WORKOUT_ID = %s"
                cursor.execute(sql, self.getWorkoutId())
                connection.commit()
                sql = "delete from WORKOUTS where WORKOUT_ID = %s"
                cursor.execute(sql, self.getWorkoutId())
                connection.commit()
        finally:
            cursor.close()
        

    @staticmethod
    def getWorkoutList(user_id):
        try:
            with connection.cursor() as cursor:
                sql = "select * FROM WORKOUTS WHERE FK_USER_ID = %s"
                cursor.execute(sql, user_id)
                info = cursor.fetchall()
        finally:
            cursor.close()
        return info
    @staticmethod
    def getUserId(workout_id):
        try:
            with connection.cursor() as cursor:
                sql = "select FK_USER_ID FROM WORKOUTS WHERE WORKOUT_ID = %s"
                cursor.execute(sql, workout_id)
                info = cursor.fetchone()
        finally:
            cursor.close()
        return int(info['FK_USER_ID'])
    
if __name__ == "__main__":
    pass