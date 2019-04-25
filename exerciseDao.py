from dbFunctions import *
from datetime import date
from apiExercises import *
from workoutDao import *
from userDao import *
class exerciseDao:
    def __init__(self,  workout_id, exercise_query, from_database = False):
        self.workoutID = workout_id
        self.userID = workoutDao.getUserId(self.workoutID)
        self.birthday = userDao.getValueOfUserInField(self.userID, "BIRTHDATE")
        self.gender = userDao.getValueOfUserInField(self.userID, "GENDER")
        self.weight = userDao.getValueOfUserInField(self.userID, "WEIGHT")
        self.height = userDao.getValueOfUserInField(self.userID, "HEIGHT")
        self.setAge()
        if from_database == False:
            self.exerciseQuery = exercise_query
            self.exerciseName = getExerciseName_s(exercise_query, self.gender, self.weight, self.height, self.age)[0]
            self.duration = getDurationByExercise(exercise_query, self.gender, self.weight, self.height, self.age)[self.exerciseName]
            self.calories = getCaloriesBurnedByExercise(exercise_query, self.gender, self.weight, self.height, self.age)[self.exerciseName]
            self.met = getMetByExercise(exercise_query, self.gender, self.weight, self.height, self.age)[self.exerciseName]
            self.createExercise()

    def createExercise(self):
        try:
            with connection.cursor() as cursor:
                sql = "insert into EXERCISES (EXERCISE_QUERY, NAME, DURATION, CALORIES, MET, FK_WORKOUT_ID) values (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (self.exerciseQuery, self.exerciseName, self.duration, self.calories, self.met, self.workoutID))
                connection.commit()
        finally:
            cursor.close()

    def deleteExercise(self):
        try:
            with connection.cursor() as cursor:
                sql = f"delete from EXERCISES where NAME = {self.exerciseName} and WORKOUT_ID = {self.workoutID}"
                cursor.execute(sql)
                connection.commit()
        finally:
            cursor.close()
            
    def setAge(self):
        today = date.today()
        self.age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    @staticmethod
    def getExerciseList(workout_id):
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