from dbFunctions import *

class workoutDao():
    def __init__(self, user_id, start_time, week_day):
        self.userID = user_id
        self.startTime = start_time
        self.weekday = week_day
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
                cursor.execute(sql, (self.startTime, self.weekday, self.userID))
                info = cursor.fetchone()
        finally:
            cursor.close()
        return int(info['WORKOUT_ID'])
    
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
    
if __name__ == "__main__":
    pass