from validate_email import validate_email
import datetime

# checks if user input is possible choice
def checkIfChoice(input, poss_options, quit_option = True):
    if quit_option == True:
        if input not in ["q", "Q"]:
            try:
                int(input)
                if int(input) in poss_options:
                    return True
                else: 
                    return False
            except ValueError:
                return False
        else:
            return True
    else:
        try:
            int(input)
            if int(input) in poss_options:
                return True
            else: 
                return False
        except ValueError:
            return False

# Checks if String is integer
def checkStringIsInt(input):
    try: 
        if input.isdigit() == True:
            return True
        else:
            return False
    except ValueError:
        return False

# Check if string is float
def checkStringIsFloat(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

# Check if input length > 0
def checkIfStringLenNeqZero(input):
    return True if len(input) != 0 else False

# Check valid height input
def checkHeight(input):
    if checkStringIsFloat(input) == True:
        input = float(input)
        if input >= 1 and input <= 2.5:
            return True
        else:
            return False
    else:
        return False

# Check valid weight
def checkWeight(input):
    if checkStringIsFloat(input) == True:
        input = float(input)
        if input >= 40 and input <= 350:
            return True
        else:
            return False
    else:
        return False

# Check email
def checkEmail(input):
    return True if validate_email(input) == True else False

# Check valid year of birth
def checkValidYearOfBirth(input):
    try:
        birthday = datetime.datetime.strptime(input, "%d.%m.%Y").date()
        if birthday > datetime.date.today():
            return False
        else:
            return True
    except:
        return False

if __name__ == "__main__":
    pass