import apiBMI 
class user():
    def __init__(self, first_name, middle_name, last_name, weight, height, username, password, e_mail, birthday, diet = None, intolerances = None):
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
        first_name, middle_name, last_name, weight, height, username, password, e_mail, birthday, diet, intolerances = arg_list
        return cls(first_name, middle_name, last_name, weight, height, username, password, e_mail, birthday, diet, intolerances)

if __name__ == "__main__":
    pass