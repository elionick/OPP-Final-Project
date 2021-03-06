from validate_email import validate_email
from userDao import *
from apiFoodNutritions import *
import datetime
from apiExercises import *
import re

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
        birthday = datetime.datetime.strptime(input, "%Y-%m-%d").date()
        if birthday > datetime.date.today():
            return False
        else:
            return True
    except:
        return False

# Check Username Input 
def checkNewUsername(input):
    if checkIfStringLenNeqZero == False:
        return False
    else:
        return not userDao.checkUsernameExists(input)

# Check diet knonw
def checkDiet(input):
    if input in ["regular", "vegetarian", "vegan"]:
        return True
    else:
        return False

# Check Intolerances
def checkIntolerances(input):
    if input == "":
        return True
    else:
        intolerances = input.split(',')
        for intolerance in intolerances:
            if apiFoodNutritions.checkFoodInApi(intolerance) == False:
                return False
    return True

# Check Intolerance Update
def checkIntoleranceUpdate(input, existing_intolerance):
    try:
        food_name_s = apiFoodNutritions.getFoodNameList(input)
    except:
        return False
    for food in food_name_s:
        if food in existing_intolerance:
            return False
    return True

def checkGender(input):
    if input in ["m", "f"]:
        return True
    return False

# Check day
def checkDayValid(input):
    if input in ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]:
        return True
    else:
        return False

# Chek valid time
def checkTimeValid(input):
    try:
        datetime.datetime.strptime(input, "%H:%M").time()
        return True
    except:
        return False

# Check if exercise
def checkExerciseValid(input):
    try:
        if len(getExerciseDataFromQuery(input).json()['exercises']) == 1:
            return True
        else:
            return False
    except:
        return False

# Check family member
def checkFamilyMember(input, own_username, family_members_usernames):
    if userDao.checkUsernameExists(input) and input != own_username and input not in family_members_usernames:
        return True
    else:
        return False

# Check address
def checkAddress(input):
    r = re.compile('.*, \d{4}')
    match = r.match(input)
    if match is not None:
        return True
    else:
        return False


if __name__ == "__main__":
    pass
