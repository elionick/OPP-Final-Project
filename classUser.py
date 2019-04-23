import apiBMI 
from userDao import *
class user():
    def __init__(self, first_name, middle_name, last_name, height, weight, e_mail, birthday, diet, intolerances, username, password):
        self.firstName = first_name
        self.middleName = middle_name
        self.lastName = last_name
        self.weight = weight
        self.height = height
        self.username = username
        self.password = password
        self.eMail = e_mail
        self.birthday = birthday
        self.diet = diet
        self.intolerances = intolerances
        # Create user if user not exists
        if userDao.checkUsernameExists(username) == False:
            # create user in database
            userDao.createUserFromList(first_name, middle_name, last_name, height, weight, e_mail, birthday, diet, intolerances, username, password)
            # update bmi in database
            userDao.setValueForUserInField(username, "BMI", apiBMI.getBMI(weight, height))
            userDao.setValueForUserInField(username, "BMI_STATUS", apiBMI.getBMIstatus(weight, height))
        self.userID = userDao.getUserID(username)
        self.valueBMI = userDao.getValueOfUserInField(username, "BMI")
        self.statusBMI  = userDao.getValueOfUserInField(username, "BMI_STATUS")
    
    def updateAttribute(self, attribute, new_value, dao_fieldname):
        setattr(self, attribute, new_value)
        userDao.setValueForUserInField(self.username, dao_fieldname, getattr(self, attribute))

    def updateWeight(self, new_weight):
        self.weight = new_weight
        userDao.setValueForUserInField(self.username, "WEIGHT", self.weight)
        self.updateBMI()

    def updateHeight(self, new_height):
        self.height = new_height
        userDao.setValueForUserInField(self.username, "HEIGHT", self.height)
        self.updateBMI()

    def updateBMI(self):
        self.valueBMI =  apiBMI.getBMI(self.weight, self.height)
        self.statusBMI = apiBMI.getBMIstatus(self.weight, self.height)
        userDao.setValueForUserInField(self.username, "BMI", self.valueBMI)
        userDao.setValueForUserInField(self.username, "BMI_STATUS", self.statusBMI)

    @classmethod
    # Construct from list
    def from_list(cls, arg_list):
        first_name, middle_name, last_name, height, weight, e_mail, birthday, diet, intolerances, username, password = arg_list
        return cls(first_name, middle_name, last_name, height, weight, e_mail, birthday, diet, intolerances, username, password)
    @classmethod
    # Construct from database
    def from_username(cls, username):
        arg_list = userDao.getUserAttributesAsList(username)
        first_name, middle_name, last_name, height, weight, e_mail, birthday, diet, intolerances, username, password = arg_list
        return cls(first_name, middle_name, last_name, height, weight, e_mail, birthday, diet, intolerances, username, password)

if __name__ == "__main__":
    pass