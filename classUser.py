import apiBMI 
from userDao import *
from datetime import date
from classWorkout import workout
class user():
    def __init__(self, first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, diet, intolerances, username, password):
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
        self.birthday = datetime.datetime.strptime(str(birthday), "%Y-%m-%d").date()
        self.setAge()
        self.diet = diet
        self.intolerances = intolerances
        # Create user if user not exists
        if userDao.checkUsernameExists(username) == False:
            # create user in database
            userDao.createUserFromList(first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, diet, intolerances, username, password)
        self.userID = userDao.getUserID(username)
        self.setBMI()
        self.setBodyFat()
        self.workouts = workout.createListOfWorkoutObjects(self.userID)

    def updateWorkouts(self):
        self.workouts = workout.createListOfWorkoutObjects(self.userID)
    
    
    # Estimate Body Fat Percentage
    def setBodyFat(self):
        self.bodyFat = 1.39 * self.valueBMI + 0.16 * self.age - 10.34 * self.genderBinary - 9

    def setAge(self):
        today = date.today()
        self.age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    def updateAttribute(self, attribute, new_value, dao_fieldname, is_password = False):
        setattr(self, attribute, new_value)
        userDao.setValueForUserInField(self.userID, dao_fieldname, getattr(self, attribute), is_password = is_password)

    def updateWeight(self, new_weight):
        self.weight = new_weight
        userDao.setValueForUserInField(self.userID, "WEIGHT", self.weight)
        self.setBMI()

    def updateHeight(self, new_height):
        self.height = new_height
        userDao.setValueForUserInField(self.userID, "HEIGHT", self.height)
        self.setBMI()

    def setBMI(self):
        self.valueBMI =  apiBMI.getBMI(self.weight, self.height)
        self.statusBMI = apiBMI.getBMIstatus(self.weight, self.height)

    @classmethod
    # Construct from list
    def from_list(cls, arg_list):
        first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, diet, intolerances, username, password = arg_list
        return cls(first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, diet, intolerances, username, password)
    @classmethod
    # Construct from database
    def from_username(cls, username):
        arg_list = userDao.getUserAttributesAsList(username)
        first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, diet, intolerances, username, password = arg_list
        return cls(first_name, middle_name, last_name, gender, height, weight, e_mail, birthday, diet, intolerances, username, password)

if __name__ == "__main__":
    pass