from workoutDao import workoutDao
from classExercise import exercise
from getFunctions import *
class workout(workoutDao):
    def __init__(self, user_id, start_time, week_day, from_database = False):
        super().__init__(user_id, start_time, week_day, from_database)
        self.workoutID = self.getWorkoutId()
        self.exercises = exercise.createListOfExerciseObjects(self.workoutID)
        self.setCalorieBurningAndDuration()
        
    
    def setCalorieBurningAndDuration(self):
        self.calorieBurning = sum(exercise.calories for exercise in self.exercises)
        self.duration = sum(exercise.duration for exercise in self.exercises)

    def printExercises(self):
        exercisesList = []
        for exercise in self.exercises:
            exercisesList.append(exercise.getExerciseAttrAsList())
        for exercise in exercisesList:
            print(exercise)
    
    def __str__(self):
        return str([self.weekday, getTimeAsStringFromTimedelta(self.startTime)])

    def updateExercises(self):
        self.exercises = exercise.createListOfExerciseObjects(self.workoutID)
        self.setCalorieBurningAndDuration()

    @classmethod
    def createListOfWorkoutObjects(cls, user_id):
        dao_workout_list = workoutDao.getWorkoutList(user_id)
        workout_list = []
        for workout in dao_workout_list:
            workout_list.append(cls(user_id, workout['TIME'], workout['WEEKDAY'], from_database = True))
        return workout_list

if __name__ == "__main__":
    pass