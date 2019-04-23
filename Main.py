from uiFunctions import *
import time
from userDao import *
from designElements import *
from menuElements import *
from getpass import getpass
from userDao import *
from classUser import *
# Show Welcome
showWelcome()
time.sleep(2)

# Initialize choice
choice = ''

# Log in
while choice not in ["q", "Q"]:
    choice = uiMenu(logInMenu, menu_title = "Login", user_instruction="What would you like to do?")
    if choice == 1:
        username = uiMenu(["Username"], menu_title = "Login", error_keys = ["username"],
        input_type = "questions", questions_check_functions = [userDao.checkUsernameExists])
        uiMenu(["Password"], menu_title = "Login", error_keys = ["password"],
        input_type = "questions", questions_check_functions = [ userDao.checkValidPassword], questions_check_functions_additional_args = [username], questions_special_input_func = [getpass])
        active_user = user.from_username(username)
        break
    if choice == 2:
        user_data = uiMenu(
            createUserProfil, 
            menu_title = "Create User Profile", 
            error_keys = [
                "name", 
                None, 
                "name", 
                "height", 
                "weight", 
                "email",
                "birth",
                "diet",
                "intolerance",
                "username",
                "password"], 
            input_type="questions", 
            questions_check_functions = [
                checkIfStringLenNeqZero, 
                None, 
                checkIfStringLenNeqZero, 
                checkHeight,
                checkWeight,
                checkEmail,
                checkValidYearOfBirth,
                checkDiet,
                checkIntolerances,
                checkUsernameNotAssigned,
                checkIfStringLenNeqZero],
            questions_special_input_func = [None, None, None, None, None, None, None, None, None, None, getpass]
            )
        active_user = user.from_list(user_data)
        break

# Main Menu
while choice not in ["q", "Q"]:
    choice = uiMenu(mainMenu, menu_title = "Main Menu", sub_title = "Hello %s! Your BMI is %.2f (%s)" % (active_user.firstName, active_user.valueBMI,active_user.statusBMI),user_instruction="What would you like to do?")
    if choice == 1:
        pass
    if choice == 2:
        choice = uiMenu(fitnessMenu, menu_title = "Fitness",user_instruction="What would you like to do?")
        if choice == 1:
            pass
        if choice == 2:
            pass
        if choice == 3:
            # Go back to main menu
            break
    if choice == 3:
        pass
    if choice == 4:
        while choice not in ["q", "Q"]:
            choice = uiMenu(logInMenu, menu_title = "Login", user_instruction="What would you like to do?")
            if choice == 1:
                username = uiMenu(["Username"], menu_title = "Login", error_keys = ["username"],
                input_type = "questions", questions_check_functions = [userDao.checkUsernameExists])
                uiMenu(["Password"], menu_title = "Login", error_keys = ["password"],
                input_type = "questions", questions_check_functions = [ userDao.checkValidPassword], questions_check_functions_additional_args = [username], questions_special_input_func = [getpass])
                active_user = user.from_username(username)
                break
            if choice == 2:
                user_data = uiMenu(
                    createUserProfil, 
                    menu_title = "Create User Profile", 
                    error_keys = [
                        "name", 
                        None, 
                        "name", 
                        "height", 
                        "weight", 
                        "email",
                        "birth",
                        "diet",
                        "intolerance",
                        "username",
                        "password"], 
                    input_type="questions", 
                    questions_check_functions = [
                        checkIfStringLenNeqZero, 
                        None, 
                        checkIfStringLenNeqZero, 
                        checkHeight,
                        checkWeight,
                        checkEmail,
                        checkValidYearOfBirth,
                        checkDiet,
                        checkIntolerances,
                        checkUsernameNotAssigned,
                        checkIfStringLenNeqZero],
                    questions_special_input_func = [None, None, None, None, None, None, None, None, None, None, getpass]
                    )
                active_user = user.from_list(user_data)
                break


# Show Quit
showQuit()