import apiBMI
from userDao import *
from datetime import date
from classWorkout import workout
from getFunctions import *
from foodLogDao import *
from apiFoodNutritions import *
from recipeDao import *
import datetime


class user():
    def __init__(self, first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, address, diet, intolerances, username, password):
        self.firstName = first_name
        self.middleName = middle_name
        self.lastName = last_name
        self.gender = gender
        if gender == "m":
            self.genderBinary = 1
        else:
            self.genderBinary = 0
        self.weight = weight
        self.height = height
        self.username = username
        self.password = password
        self.eMail = e_mail
        self.address = address
        self.birthday = datetime.datetime.strptime(str(birthday), "%Y-%m-%d").date()
        self.setAge()
        self.diet = diet
        self.setIntolerances(intolerances)
        # Create user if user not exists
        if userDao.checkUsernameExists(username) == False:
            # create user in database
            userDao.createUserFromList(first_name, middle_name, last_name, gender, height, weight, e_mail,
                                       birthday, address, diet, apiFoodNutritions.getFoodNameString(intolerances), username, password)
        self.userID = userDao.getUserID(username)
        self.setTodaysCaloricIntake()
        self.setBMI()
        self.setBodyFat()
        self.setNetWeightandRestCalorieBurn()
        self.setWeightGoal()
        self.updateWorkouts()
        self.setFamilyMembers()
        self.setCalorieNeed()
        self.setNetCalorieNeed()
        self.setFavRecipes()

    def setIntolerances(self, intolerances):
        if intolerances == "" or intolerances == []:
            self.intolerancesList = []
            self.intolerances = ""
        elif isinstance(intolerances, str):
            self.intolerancesList = intolerances.split(",")
            self.intolerances = intolerances
        elif isinstance(intolerances, list):
            self.intolerancesList = intolerances
            self.intolerances = ", ".join(intolerances)

    def setTodaysCaloricIntake(self):
        self.CaloricIntake = foodLogDao.getTodaysCaloricIntake(self.userID)
        if self.CaloricIntake is not None:
            pass
        else:
            self.CaloricIntake = 0

    def setNetWeightandRestCalorieBurn(self):
        self.netWeight = self.weight * (1-self.bodyFat/100)
        # Katch-McArdle formula
        self.restingCalorieConsumption = 370 + (21.6 * self.netWeight)

    def setWeightGoal(self):
        self.weightGoal = userDao.getWeightGoal(self.userID)

    def setNetCalorieNeed(self):
        if self.weightGoal is not None:
            if self.weightGoal < self.weight:
                self.netCalorieNeed = self.todaysCalorieBurning * 0.85 - self.CaloricIntake
            elif self.weightGoal > self.weight:
                self.netCalorieNeed = self.todaysCalorieBurning * 1.15 - self.CaloricIntake
            else:
                self.netCalorieNeed = self.todaysCalorieBurning - self.CaloricIntake
        else:
            self.netCalorieNeed = self.todaysCalorieBurning - self.CaloricIntake

    def setCalorieNeed(self):
        if self.weightGoal is not None:
            if self.weightGoal < self.weight:
                self.calorieNeed = self.todaysCalorieBurning * 0.85
            elif self.weightGoal > self.weight:
                self.calorieNeed = self.todaysCalorieBurning * 1.15
            else:
                self.calorieNeed = self.todaysCalorieBurning
        else:
            self.calorieNeed = self.todaysCalorieBurning

    def updateWorkouts(self):
        self.setWorkouts()
        self.setTodaysCalorieBurningAndDuration()
        self.setNextWorkout()
        self.setCalorieNeed()
        self.setNetCalorieNeed()

    def __str__(self):
        return str([self.firstName, self.lastName])

    def setNextWorkout(self):
        workouts_weekdays = [getWeekdayNumber(workout.weekday) for workout in self.workouts]
        workouts_time = [(datetime.datetime.min + workout.startTime).time()
                         for workout in self.workouts]
        todays_day = datetime.datetime.today().weekday()
        current_time = datetime.datetime.now().time()
        possible_workouts = []
        for next_weekday, next_time, next_workout in zip(workouts_weekdays, workouts_time, self.workouts):
            if next_weekday == todays_day and next_time >= current_time:
                possible_workouts.append(next_workout)
        if len(possible_workouts) != 0:
            self.nextWorkout = possible_workouts[0]
        else:
            for next_weekday, next_workout in zip(workouts_weekdays, self.workouts):
                if next_weekday > todays_day:
                    possible_workouts.append(next_workout)
            if len(possible_workouts) != 0:
                self.nextWorkout = possible_workouts[0]
            else:
                for next_weekday, next_workout in zip(workouts_weekdays, self.workouts):
                    if next_weekday < todays_day:
                        possible_workouts.append(next_workout)
                if len(possible_workouts) != 0:
                    self.nextWorkout = possible_workouts[0]
                else:
                    for next_weekday, next_workout in zip(workouts_weekdays, self.workouts):
                        if next_weekday == todays_day:
                            possible_workouts.append(next_workout)
                    if len(possible_workouts) != 0:
                        self.nextWorkout = possible_workouts[0]
                    else:
                        self.nextWorkout = False

    def setTodaysCalorieBurningAndDuration(self):
        self.todaysWorkoutCalorieBurning = sum(workout.calorieBurning for workout in self.workouts if getWeekdayNumber(
            workout.weekday) == datetime.datetime.today().weekday())
        self.todaysCalorieBurning = self.todaysWorkoutCalorieBurning + self.restingCalorieConsumption
        self.todaysDuration = sum(workout.duration for workout in self.workouts if getWeekdayNumber(
            workout.weekday) == datetime.datetime.today().weekday())

    def setFamilyMembers(self):
        family_members = []
        for family_member_username in userDao.getFamilyMembersUsername(self.userID):
            family_members.append(user.from_username(family_member_username))
        self.familyMembers = family_members
        self.familyMembersUsernames = [user.username for user in self.familyMembers]

    def setWorkouts(self):
        self.workouts = workout.createListOfWorkoutObjects(self.userID)
        self.workouts = sorted(self.workouts, key=lambda x: (
            getTimeAsStringFromTimedelta(getattr(x, "startTime"))), reverse=True)
        self.workouts = sorted(self.workouts, key=lambda x: (
            getWeekdayNumber(getattr(x, "weekday"))))

    # Estimate Body Fat Percentage
    def setBodyFat(self):
        self.bodyFat = 1.39 * self.valueBMI + 0.16 * self.age - 10.34 * self.genderBinary - 9

    def setAge(self):
        today = date.today()
        self.age = today.year - self.birthday.year - \
            ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    def updateAttribute(self, attribute, new_value, dao_fieldname, is_password=False):
        setattr(self, attribute, new_value)
        userDao.setValueForUserInField(self.userID, dao_fieldname, getattr(
            self, attribute), is_password=is_password)

    def updateWeight(self, new_weight):
        self.weight = new_weight
        userDao.setValueForUserInField(self.userID, "WEIGHT", self.weight)
        self.setBMI()
        self.setBodyFat()
        self.setNetWeightandRestCalorieBurn()
        self.setTodaysCalorieBurningAndDuration()
        self.setCalorieNeed()
        self.setNetCalorieNeed()

    def setFavRecipes(self):
        if getRecipeList(self.userID) == ():
            self.favrecipe = []
        else:
            self.favrecipe = getRecipeList(self.userID)

        self.favrecipeshort = []
        for each in self.favrecipe:
            self.favrecipeshort.append(each["RECIPE_NAME"])

    def updateHeight(self, new_height):
        self.height = new_height
        userDao.setValueForUserInField(self.userID, "HEIGHT", self.height)
        self.setBMI()
        self.setBodyFat()
        self.setNetWeightandRestCalorieBurn()
        self.setTodaysCalorieBurningAndDuration()
        self.setCalorieNeed()
        self.setNetCalorieNeed()

    def setBMI(self):
        self.valueBMI = apiBMI.getBMI(self.weight, self.height)
        self.statusBMI = apiBMI.getBMIstatus(self.weight, self.height)

    @classmethod
    # Construct from list
    def from_list(cls, arg_list):
        first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, address, diet, intolerances, username, password = arg_list
        return cls(first_name, middle_name, last_name, gender, float(height), float(weight), e_mail, birthday, address, diet, intolerances, username, password)

    @classmethod
    # Construct from database
    def from_username(cls, username):
        arg_list = userDao.getUserAttributesAsList(username)
        first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, address, diet, intolerances, username, password = arg_list
        return cls(first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, address, diet, intolerances, username, password)


if __name__ == "__main__":
    pass
