from workoutDao import workoutDao
class workout(workoutDao):
    def createNewWorkout(self):
        self.setWorkout()    
    
    @classmethod
    def createListOfWorkoutObjects(cls, user_id):
        dao_workout_list = workoutDao.getWorkoutList(user_id)
        workout_list = []
        for workout in dao_workout_list:
            workout_list.append(cls(user_id, workout['TIME'], workout['WEEKDAY']))
        return workout_list

if __name__ == "__main__":
    w_list = workout.createListOfWorkoutObjects(24)