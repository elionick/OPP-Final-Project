from uiFunctions import *
import time
from userDao import *
from designElements import *
from menuElements import *
from getpass import getpass
from classUser import *
from classWorkout import workout
from classExercise import exercise
from apiRecipe import *
from recipeDao import *

# Show Welcome
showWelcome()
time.sleep(2)

# Initialize choice
choice = ''

# Log in
while choice not in ["q", "Q"]:
    choice = uiMenu(logInMenu, menu_title = "Login", user_instruction="What would you like to do?")
    if choice == 1:
        global username
        username = uiMenu(["Username"], menu_title = "Login", error_keys = ["username"],
        input_type = "questions", questions_check_functions = [userDao.checkUsernameExists])
        uiMenu(["Password"], menu_title = "Login", error_keys = ["password"],
        input_type = "questions", questions_check_functions = [userDao.checkValidPassword], questions_check_functions_additional_args = [username], questions_special_input_func = [getpass])
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
    choice = uiMenu(mainMenu, menu_title = "Main Menu", sub_title = "Hello %s! Your BMI is %.2f (%s). Your Body Fat is %.2f%%.\n\nNext workout at:\t\t\t%s on %s\nWorkout Duration:\t\t\t%.2f minutes\nWorkout calorie burning:\t\t%.2f\n\nToday's stats:\nResting calorie consumption:\t\t%.2f\nWorkout(s) calorie consumption:\t\t%.2f\nTotal calorie consumption:\t\t%.2f\nCalorie requirement:\t\t\t%.2f\nTotal workout duration:\t\t\t%.2f minutes" % (active_user.firstName, active_user.valueBMI,active_user.statusBMI, active_user.bodyFat, str(active_user.nextWorkout.startTime).split(":")[0] + ":" + str(active_user.nextWorkout.startTime).split(":")[1] if active_user.nextWorkout != False else "--", active_user.nextWorkout.weekday if active_user.nextWorkout != False else "--",active_user.nextWorkout.duration if active_user.nextWorkout != False else 0, active_user.nextWorkout.calorieBurning if active_user.nextWorkout != False else 0, active_user.restingCalorieConsumption, active_user.todaysWorkoutCalorieBurning,  active_user.todaysCalorieBurning, active_user.calorieNeed, active_user.todaysDuration),user_instruction="What would you like to do?")
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
        while choice not in ["q", "Q"]:
            # Recipes
            choice = uiMenu(recipesMenu, menu_title = "Recipes",user_instruction="What would you like to do?")
            info = userDao.getUserAttributesAsList(username)
            User_ID = userDao.getUserID(username)
            if choice == 1:
                getRecipeByIngredients(User_ID)
                pass
            if choice == 2:
                getRecipeByMeal(User_ID, info[9], info[8])
                pass
            if choice == 3:
                chooseRecipe(User_ID)
                pass
            if choice == 4:
                # Go back to main menu
                break
    if choice == 3:
        while choice not in ["q", "Q"]:
            # Fitness
            choice = uiMenu(fitnessMenu, menu_title = "Fitness",user_instruction="What would you like to do?")
            if choice == 1:
                workout_data = uiMenu(createNewWorkout, menu_title="Create New Workout", input_type="questions", error_keys=["day", "time"], questions_check_functions=[checkDayValid, checkTimeValid])
                new_workout = workout(active_user.userID, workout_data[1], workout_data[0])
                # Menu to add exercises to workout
                while choice not in ["q", "Q"]:
                    choice = uiMenu(specifyWorkout, menu_title = "Specify Workout", sub_title = "Workout's exercises:", sub_sub_title = new_workout.printExercises,user_instruction="What would you like to do?")
                    if choice == 1:
                        exercise_data = uiMenu(["Enter exercise"], menu_title="Add Exercise", input_type="questions", error_keys=["exercise"], questions_check_functions=[checkExerciseValid])
                        new_exercise = exercise(new_workout.workoutID, exercise_data[0])
                        new_workout.updateExercises()
                        active_user.updateWorkouts()
                    if choice == 2:
                        active_user.updateWorkouts()
                        choice = ''
                        break
            if choice == 2:
                while choice not in ["q", "Q"]:
                    # Workout Plan 
                    choice = uiMenu(active_user.workouts + ["Go back to Fitness Menu"], menu_title = "Weekly Workouts", user_instruction="Choose a workout to see details:")
                    if choice == len(active_user.workouts) + 1:
                        choice = ''
                        break
                    elif choice in ["q", "Q"]:
                        break
                    else:
                        workout_chosen = active_user.workouts[choice - 1]
                        while choice not in ["q", "Q"]:
                            choice = uiMenu(["Add exercise", "Delete Exercise", "Go back to weekly workouts menu"], menu_title = "Exercises", sub_title = "Exercises of this workout:", sub_sub_title =getattr(workout_chosen, "printExercises"),user_instruction="What would you like to do?")
                            if choice == 1:
                                exercise_data = uiMenu(["Enter exercise"], menu_title="Add Exercise", input_type="questions", error_keys=["exercise"], questions_check_functions=[checkExerciseValid])
                                new_exercise = exercise(workout_chosen.workoutID, exercise_data[0])
                                workout_chosen.updateExercises()
                                active_user.updateWorkouts()
                            if choice == 2:
                                while choice not in ["q", "Q"]:
                                    choice = uiMenu(workout_chosen.exercises + ["Go back to Exercises"], menu_title = "Delete Exercises", user_instruction="Which exercise do you want to delete?:")
                                    if choice == len(workout_chosen.exercises) + 1:
                                        choice = ''
                                        break
                                    elif choice in ["q", "Q"]:
                                        break
                                    else:
                                        exercise_chosen = workout_chosen.exercises[choice - 1]
                                        exercise_chosen.deleteExercise()
                                        workout_chosen.updateExercises()
                                        active_user.updateWorkouts()
                            if choice == 3:
                                choice = ''
                                break
            if choice == 3:
                # Delete Workout
                choice = uiMenu(active_user.workouts + ["Go back to Fitness Menu"], menu_title = "Weekly Workouts", user_instruction="Choose a workout to delete:")    
                if choice == len(active_user.workouts) + 1:
                    choice = ''
                    break
                elif choice in ["q", "Q"]:
                    break
                else:
                    workout_chosen = active_user.workouts[choice - 1]
                    workout_chosen.deleteWorkout()
                    active_user.updateWorkouts()
            if choice == 4:
                choice = ''
                # Go back to main menu
                break
    if choice == 4:
        pass
    if choice == 5:
        while True:
            choice = uiMenu(active_user.familyMembers + ["Add Family Member","Go back to Main Menu"], menu_title = "Family Members", user_instruction="Choose a family member to delete or another option:")
            if choice == len(active_user.familyMembers) + 2:
                choice = ''
                break
            elif choice in ["q", "Q"]:
                break
            elif choice == len(active_user.familyMembers) + 1:
                # Add Family Member
                family_member_username = uiMenu(["Enter username of family member"], menu_title="Add Family Member", input_type="questions", error_keys=["username"], questions_check_functions=[checkFamilyMember], questions_check_functions_additional_args=[[active_user.username, active_user.familyMembersUsernames]])
                userDao.addFamilyMember(active_user.userID, family_member_username)
                active_user.setFamilyMembers()
            else:
                # Delete Family Member
                userDao.deleteFamilyMember(active_user.userID, active_user.familyMembers[choice - 1].userID)
                active_user.setFamilyMembers()
    if choice == 6:
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