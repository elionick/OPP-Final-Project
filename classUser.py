from apiBMI import *
class user():
    def __init__(self, first_name, middle_names, last_name, weight, height, username, password, e_mail, birthday):
        self.firstName = first_name
        self.middleNames = middle_names
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
    Eddie = user("Eddie", "Alexander", "Guenther", 70, 1.83, "Eddie", 2403, "eddie.guenther@yahoo.de")
    print(Eddie.bmi)
    Eddie.setAllergies("Fruits", "Milk")
    print(Eddie.nAllergies)
    print(Eddie.allergy1)
    print(Eddie.statusBMI)