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
        self.bmi = apiBMI.getBMI(weight, height)
        self.statusBMI  = apiBMI.getBMIstatus(weight, height)
        self.birthday = birthday
        self.diet = diet
        self.intolerances = intolerances

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