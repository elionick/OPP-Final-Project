from apiBMI import *
from userDao import *
class user():
    def __init__(self, first_name, middle_name, last_name, weight, height, username, password, e_mail, birthday):
        self.firstName = first_name
        self.middleName = middle_name
        self.lastName = last_name
        self.weight = weight
        self.height = height
        self.username = username
        self.password = password
        self.eMail = e_mail
        self.bmi = getBMI(weight, height)
        self.statusBMI  = getBMIstatus(weight, height)
        self.birthday = birthday

    def setAllergies(self, *allergies):
        for index, allergy in enumerate(allergies):
            setattr(self, "allergy" + str(index), allergy)
        setattr(self, "nAllergies", len(allergies))

if __name__ == "__main__":
    pass