from uiFunctions import *
import time
from designElements import *
from menuElements import *
from getpass import getpass

# Show Welcome
showWelcome()
time.sleep(2)

# Initialize choice
choice = ''

# Log in
while choice not in ["q", "Q"]:
    choice = uiMenu(logIn, menu_title = "Login", user_instruction="What would you like to do?")
    if choice == 1:
        pass
    if choice == 2:
        # to fix:
        # - username and password have to be unique
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
                checkIfStringLenNeqZero,
                checkIfStringLenNeqZero],
            questions_special_input_func = [None, None, None, None, None, None, None, None, getpass]
            )
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
        while True:
            choice = uiMenu(logIn, menu_title = "Login", user_instruction="What would you like to do?")
            if choice == 1:
                pass
            if choice == 2:
                # to fix:
                # - username and password have to be unique
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
                        checkIfStringLenNeqZero,
                        checkIfStringLenNeqZero],
                    questions_special_input_func = [None, None, None, None, None, None, None, None, getpass]
                    )
                break

# Show Quit
showQuit()