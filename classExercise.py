from exerciseDao import exerciseDao
class exercise(exerciseDao):
    def __init__(self, workout_id, exercise_query, exercise_name=None, duration=None, calories=None, met=None, from_database = False):
        super().__init__(workout_id, exercise_query, from_database)
        if from_database == True:
            self.exerciseQuery = exercise_query
            self.exerciseName = exercise_name
            self.duration = duration
            self.calories = calories
            self.met = met
    
    def getExerciseAttrAsList(self):
        return [self.exerciseQuery, self.exerciseName, self.duration, self.calories, self.met]


    @classmethod
    def createListOfExerciseObjects(cls, workout_id):
        dao_exercise_list = exerciseDao.getExerciseList(workout_id)
        exercise_list = []
        for exercise in dao_exercise_list:
            exercise_list.append(cls(workout_id, exercise['EXERCISE_QUERY'], exercise['NAME'], exercise['DURATION'], exercise['CALORIES'], exercise['MET'], from_database = True))
        return exercise_list    