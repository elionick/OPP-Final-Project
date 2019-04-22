from uiFunctions import *
import time
from designElements import *
from menuElements import *
from getpass import getpass
from userDao import *
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
        input_type = "questions", questions_check_functions = [checkUsernameExists])
        uiMenu(["Password"], menu_title = "Login", error_keys = ["password"],
        input_type = "questions", questions_check_functions = [ checkValidPassword], questions_check_functions_additional_args = [username], questions_special_input_func = [getpass])
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
        createUser(user_data[7], password = user_data[8], first_name = user_data[0], middle_name = user_data[1], last_name = user_data[2], height = user_data[3], weight = user_data[4], birthdate = user_data[6], email = user_data[5])
        break

# Main Menu
while choice not in ["q", "Q"]:
    choice = uiMenu(mainMenu, menu_title = "Main Menu", user_instruction="What would you like to do?")
    if choice == 1:
        pass
    if choice == 2:
        pass
    if choice == 3:
        pass
    if choice == 4:
        pass

# Show Quit
showQuit()