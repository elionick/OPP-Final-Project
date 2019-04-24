from uiFunctions import *
import time
from userDao import *
from designElements import *
from menuElements import *
from getpass import getpass
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
                "gender",
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
                checkGender,
                checkHeight,
                checkWeight,
                checkEmail,
                checkValidYearOfBirth,
                checkDiet,
                checkIntolerances,
                checkNewUsername,
                checkIfStringLenNeqZero],
            questions_special_input_func = [None, None, None, None, None, None, None, None, None, None, None, getpass]
            )
        active_user = user.from_list(user_data)
        break

# Main Menu
while choice not in ["q", "Q"]:
    choice = uiMenu(mainMenu, menu_title = "Main Menu", sub_title = "Hello %s! Your BMI is %.2f (%s)" % (active_user.firstName, active_user.valueBMI,active_user.statusBMI),user_instruction="What would you like to do?")
    if choice == 1:
        while choice not in ["q", "Q"]:
            # Update profile information
            choice = uiMenu(updateProfileInformationMenu, menu_title = "Update Profile Information",user_instruction = "What information would you like to update?")
            if choice == 1:
                # Update first name
                new_first_name = uiMenu(["Enter new first name"], menu_title = "Update First Name", input_type="questions", error_keys=["name"], questions_check_functions=[checkIfStringLenNeqZero])[0]
                active_user.updateAttribute("firstName", new_first_name, "FIRST_NAME")
            if choice == 2:
                # Update middle name
                new_middle_name = uiMenu(["Enter new middle name"], menu_title = "Update Middle Name", input_type="questions")[0]
                active_user.updateAttribute("middleName", new_middle_name, "MIDDLE_NAME")
            if choice == 3:
                # Update last name
                new_last_name = uiMenu(["Enter new last name"], menu_title = "Update Last Name", input_type="questions",error_keys=["name"], questions_check_functions=[checkIfStringLenNeqZero])[0]
                active_user.updateAttribute("lastName", new_last_name, "LAST_NAME")
            if choice == 4:
                new_gender = uiMenu(["Enter new gender"], menu_title = "Update Gender", input_type="questions",error_keys=["gender"], questions_check_functions=[checkGender])[0]
                active_user.updateAttribute("gender", new_gender, "GENDER")
            if choice == 5:
                # Update height
                new_height = uiMenu(["Enter new height (in meter)"], menu_title = "Update Height", input_type="questions",error_keys=["height"], questions_check_functions=[checkHeight])[0]
                active_user.updateHeight(new_height)
            if choice == 6:
                # Update weight
                new_weight = uiMenu(["Enter new weight (in kilogram)"], menu_title = "Update Weight", input_type="questions",error_keys="weight", questions_check_functions=[checkWeight])[0]
                active_user.updateWeight(new_weight)
            if choice == 7:
                # Update email
                new_email = uiMenu(["Enter new email"], menu_title = "Update Email", input_type="questions",error_keys=["email"], questions_check_functions=[checkEmail])[0]
                active_user.updateAttribute("eMail", new_email, "E_MAIL")
            if choice == 8:
                # Update birthday
                new_birthday = uiMenu(["Enter new birthday"], menu_title = "Update Birthday", input_type="questions",error_keys=["birth"], questions_check_functions=[checkValidYearOfBirth])[0]
                active_user.updateAttribute("birthday", new_birthday, "BIRTHDATE")
            if choice == 9:
                # Update diet
                new_diet = uiMenu(["Enter new diet"], menu_title = "Update Diet", input_type="questions",error_keys=["diet"], questions_check_functions=[checkDiet])[0]
                active_user.updateAttribute("diet", new_diet, "DIET")
            if choice == 10:
                # to do: Intolerance Add and Delete Option
                pass
            if choice == 11:
                # Update username
                new_username = uiMenu(["Enter new username"], menu_title = "Update Username", input_type="questions", error_keys=["username"], questions_check_functions=[checkNewUsername])[0]
                active_user.updateAttribute("username", new_username, "LOGIN_NAME")
            if choice == 12:
                # Update password
                new_password = uiMenu(["Enter new password"], menu_title = "Update Password", input_type="questions", error_keys=["password"], questions_check_functions=[checkIfStringLenNeqZero], questions_special_input_func = [getpass])[0]
                active_user.updateAttribute("password", new_password, "PASSWORD_HASH", is_password = True)
            if choice == 13:
                # Go back to main menu
                break
    if choice == 2:
        pass
    if choice == 3:
        while choice not in ["q", "Q"]:
            # Fitness
            choice = uiMenu(fitnessMenu, menu_title = "Fitness",user_instruction="What would you like to do?")
            if choice == 1:
                pass
            if choice == 2:
                pass
            if choice == 3:
                # Go back to main menu
                break
    if choice == 4:
        pass
    if choice == 5:
        # Logout
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
                        "gender",
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
                        checkGender, 
                        checkHeight,
                        checkWeight,
                        checkEmail,
                        checkValidYearOfBirth,
                        checkDiet,
                        checkIntolerances,
                        checkNewUsername,
                        checkIfStringLenNeqZero],
                    questions_special_input_func = [None, None, None, None, None, None, None, None, None, None, None, getpass]
                    )
                active_user = user.from_list(user_data)
                break


# Show Quit
showQuit()