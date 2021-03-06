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
from apiMap import *
from classShoppingList import *
# Show Welcome
showWelcome()
time.sleep(2)

# Initialize choice
choice = ''

# Log in
while choice not in ["q", "Q"]:
    choice = uiMenu(logInMenu, menu_title="Login", user_instruction="What would you like to do?")
    if choice == 1:
        username = uiMenu(["Username"], menu_title="Login", error_keys=["username"],
                          input_type="questions", questions_check_functions=[userDao.checkUsernameExists])
        uiMenu(["Password"], menu_title="Login", error_keys=["password"],
               input_type="questions", questions_check_functions=[userDao.checkValidPassword], questions_check_functions_additional_args=[username], questions_special_input_func=[getpass])
        active_user = user.from_username(username)
        break
    if choice == 2:
        user_data = uiMenu(
            createUserProfil,
            menu_title="Create User Profile",
            error_keys=[
                "name",
                None,
                "name",
                "gender",
                "height",
                "weight",
                "email",
                "birth",
                "address",
                "diet",
                "intolerance",
                "username",
                "password"],
            input_type="questions",
            questions_check_functions=[
                checkIfStringLenNeqZero,
                None,
                checkIfStringLenNeqZero,
                checkGender,
                checkHeight,
                checkWeight,
                checkEmail,
                checkValidYearOfBirth,
                checkAddress,
                checkDiet,
                checkIntolerances,
                checkNewUsername,
                checkIfStringLenNeqZero],
            questions_special_input_func=[None, None, None, None,
                                          None, None, None, None, None, None, None, None, getpass]
        )
        active_user = user.from_list(user_data)
        break

# Main Menu
while choice not in ["q", "Q"]:
    choice = uiMenu(mainMenu, menu_title="Main Menu", sub_title="Hello %s! Your BMI is %.2f (%s). Your Body Fat is %.2f%%.\n\nNext workout at:\t\t\t%s on %s\nWorkout Duration:\t\t\t%.2f minutes\nWorkout calorie burning:\t\t%.2f\n\nToday's stats:\nResting calorie burning:\t\t%.2f\nWorkout(s) calorie burning:\t\t%.2f\nTotal calorie burning:\t\t\t%.2f\nCalorie intake:\t\t\t\t%.2f from %.2f calories needed\nTotal workout duration:\t\t\t%.2f minutes" % (active_user.firstName, active_user.valueBMI, active_user.statusBMI, active_user.bodyFat, str(active_user.nextWorkout.startTime).split(":")[0] + ":" + str(
        active_user.nextWorkout.startTime).split(":")[1] if active_user.nextWorkout != False else "--", active_user.nextWorkout.weekday if active_user.nextWorkout != False else "--", active_user.nextWorkout.duration if active_user.nextWorkout != False else 0, active_user.nextWorkout.calorieBurning if active_user.nextWorkout != False else 0, active_user.restingCalorieConsumption, active_user.todaysWorkoutCalorieBurning,  active_user.todaysCalorieBurning, active_user.CaloricIntake, active_user.calorieNeed, active_user.todaysDuration), user_instruction="What would you like to do?")
    if choice == 1:
        while choice not in ["q", "Q"]:
            # Update profile information
            choice = uiMenu(updateProfileInformationMenu, menu_title="Update Profile Information",
                            user_instruction="What information would you like to update?")
            if choice == 1:
                # Update first name
                new_first_name = uiMenu(["Enter new first name"], menu_title="Update First Name", input_type="questions", error_keys=[
                                        "name"], questions_check_functions=[checkIfStringLenNeqZero])[0]
                active_user.updateAttribute("firstName", new_first_name, "FIRST_NAME")
            if choice == 2:
                # Update middle name
                new_middle_name = uiMenu(["Enter new middle name"],
                                         menu_title="Update Middle Name", input_type="questions")[0]
                active_user.updateAttribute("middleName", new_middle_name, "MIDDLE_NAME")
            if choice == 3:
                # Update last name
                new_last_name = uiMenu(["Enter new last name"], menu_title="Update Last Name", input_type="questions", error_keys=[
                                       "name"], questions_check_functions=[checkIfStringLenNeqZero])[0]
                active_user.updateAttribute("lastName", new_last_name, "LAST_NAME")
            if choice == 4:
                new_gender = uiMenu(["Enter new gender"], menu_title="Update Gender", input_type="questions", error_keys=[
                                    "gender"], questions_check_functions=[checkGender])[0]
                active_user.updateAttribute("gender", new_gender, "GENDER")
            if choice == 5:
                # Update height
                new_height = uiMenu(["Enter new height (in meter)"], menu_title="Update Height", input_type="questions", error_keys=[
                                    "height"], questions_check_functions=[checkHeight])[0]
                active_user.updateHeight(new_height)
            if choice == 6:
                # Update weight
                new_weight = uiMenu(["Enter new weight (in kilogram)"], menu_title="Update Weight",
                                    input_type="questions", error_keys="weight", questions_check_functions=[checkWeight])[0]
                active_user.updateWeight(new_weight)
            if choice == 7:
                # Update email
                new_email = uiMenu(["Enter new email"], menu_title="Update Email", input_type="questions", error_keys=[
                                   "email"], questions_check_functions=[checkEmail])[0]
                active_user.updateAttribute("eMail", new_email, "E_MAIL")
            if choice == 8:
                # Update birthday
                new_birthday = uiMenu(["Enter new birthday"], menu_title="Update Birthday", input_type="questions", error_keys=[
                                      "birth"], questions_check_functions=[checkValidYearOfBirth])[0]
                active_user.updateAttribute("birthday", new_birthday, "BIRTHDATE")
            if choice == 9:
                # Update address
                new_address = uiMenu(["Enter new address"], menu_title="Update Address", input_type="questions", error_keys=[
                                     "address"], questions_check_functions=[checkAddress])[0]
                active_user.updateAttribute("address", new_address, "ADDRESS")
            if choice == 10:
                # Update diet
                new_diet = uiMenu(["Enter new diet"], menu_title="Update Diet", input_type="questions", error_keys=[
                                  "diet"], questions_check_functions=[checkDiet])[0]
                active_user.updateAttribute("diet", new_diet, "DIET")
            if choice == 11:
                # to do: Intolerance Add and Delete Option
                while choice not in ["q", "Q"]:
                    choice = uiMenu(["Add intolerance", "Delete intolerance", "Go back to update profile information"],
                                    menu_title="Intolerances", user_instruction="What would you like to do?")
                    if choice == 1:
                        # Add intolerance
                        new_intolerance = uiMenu(["Enter new intolerance"], menu_title="Update Intolerances", input_type="questions", error_keys=[
                                                 "intolerance"], questions_check_functions=[checkIntoleranceUpdate], questions_check_functions_additional_args=[[active_user.intolerancesList]])[0]
                        new_intolerance = apiFoodNutritions.getFoodNameString(new_intolerance)
                        if active_user.intolerances == "":
                            active_user.setIntolerances(new_intolerance)
                        else:
                            active_user.setIntolerances(
                                active_user.intolerances + "," + new_intolerance)
                        userDao.setValueForUserInField(
                            active_user.userID, "INTOLERANCE", active_user.intolerances)
                    if choice == 2:
                        while choice not in ["q", "Q"]:
                            # delete intolerance
                            choice = uiMenu(active_user.intolerancesList + ["Go back to update profile information"] if active_user.intolerances is not "" else [
                                            "Go back to update profile information"], menu_title="Delete Intolerances", user_instruction="Which intolerance would you like to delete?")
                            if choice == len(active_user.intolerancesList) + 1 if active_user.intolerances is not "" else 1:
                                choice = ''
                                break
                            elif choice in ["q", "Q"]:
                                break
                            else:
                                new_intolerance = list(active_user.intolerancesList)
                                new_intolerance.pop(choice - 1)
                                active_user.setIntolerances(new_intolerance)
                                userDao.setValueForUserInField(
                                    active_user.userID, "INTOLERANCE", active_user.intolerances)
                    if choice == 3:
                        choice = ''
                        break
            if choice == 12:
                # Update username
                new_username = uiMenu(["Enter new username"], menu_title="Update Username", input_type="questions", error_keys=[
                                      "username"], questions_check_functions=[checkNewUsername])[0]
                active_user.updateAttribute("username", new_username, "LOGIN_NAME")
            if choice == 13:
                # Update password
                new_password = uiMenu(["Enter new password"], menu_title="Update Password", input_type="questions", error_keys=[
                                      "password"], questions_check_functions=[checkIfStringLenNeqZero], questions_special_input_func=[getpass])[0]
                active_user.updateAttribute("password", new_password,
                                            "PASSWORD_HASH", is_password=True)
            if choice == 14:
                # Go back to main menu
                break
    if choice == 2:
        while choice not in ["q", "Q"]:
            # Recipes
            choice = uiMenu(recipesMenu, menu_title="Recipes",
                            user_instruction="What would you like to do?")

            if choice in [1, 2]:
                if userDao.getFamilyMemberUserID(active_user.userID) == []:
                    recipe = apiRecipe(active_user.userID,  active_user.intolerances, active_user.diet)
                else:
                    question = uiMenu(recipesFamilyMenu, menu_title="Family Recipes", user_instruction="Do you want to cook with your family or alone?")
                    if question == 1:
                        recipe = apiRecipe(active_user.userID,  active_user.intolerances, active_user.diet)
                    if question == 2:
                        familyMembers = list(userDao.getFamilyMemberUserID  (active_user.userID))
                        familyMembers.append(active_user.userID)
                        memberDiet = list()
                        Intolerance = list()
                        i = 0
                        while i < len(familyMembers):
                            Intolerance += userDao.getIntolerance(familyMembers [i])
                            i += 1
                        i = 0
                        while i < len(familyMembers):
                            memberDiet.append(userDao.getDiet(familyMembers[i]))
                            i += 1
                        if "vegan" in memberDiet:
                            Diet = "vegan"
                        elif "vegetarian" in memberDiet:
                            Diet = "vegetarian"
                        else:
                            Diet = "regular"
                        Intolerance = str(Intolerance)
                        Intolerance = Intolerance[1:-1]
                        recipe = apiRecipe(active_user.userID, Intolerance,     Diet)
                    if question == 3:
                        # go back
                        choice = ""
                        break
                    if question in ["q", "Q"]:
                        choice = "q"
                        break

            if choice == 1:
                recipe.getRecipeByIngredients()
                active_user.setTodaysCaloricIntake()
                pass
            if choice == 2:
                recipe.getRecipeByMeal()
                active_user.setTodaysCaloricIntake()
                pass
            if choice == 3:
                while choice not in ["q", "Q"]:
                    choice = uiMenu(favRecipeMenu, menu_title="Favourite recipes",
                                user_instruction="What would you like to do?")
                    if choice == 1:
                        chooseRecipe(active_user.userID)
                        pass
                    if choice == 2:
                        deleteRecipe(active_user.userID)
                        active_user.setFavRecipes()
                        pass

                    if choice == 3:
                        # Go back to recipe menu
                        choice = ''
                        break
            if choice == 4:
                # Go back to main menu
                choice = ''
                break
        if choice == 4:
            # Go back to main menu
            choice = ''
            break
    if choice == 3:
        while choice not in ["q", "Q"]:
            # Fitness
            choice = uiMenu(fitnessMenu, menu_title="Fitness",
                            user_instruction="What would you like to do?")
            if choice == 1:
                workout_data = uiMenu(createNewWorkout, menu_title="Create New Workout", input_type="questions", error_keys=[
                                      "day", "time"], questions_check_functions=[checkDayValid, checkTimeValid])
                new_workout = workout(active_user.userID, workout_data[1], workout_data[0])
                # Menu to add exercises to workout
                while choice not in ["q", "Q"]:
                    choice = uiMenu(specifyWorkout, menu_title="Specify Workout", sub_title="Workout's exercises:",
                                    sub_sub_title=new_workout.printExercises, user_instruction="What would you like to do?")
                    if choice == 1:
                        exercise_data = uiMenu(["Enter exercise"], menu_title="Add Exercise", input_type="questions", error_keys=[
                                               "exercise"], questions_check_functions=[checkExerciseValid])
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
                    choice = uiMenu(active_user.workouts + ["Go back to Fitness Menu"],
                                    menu_title="Weekly Workouts", user_instruction="Choose a workout to see details:")
                    if choice == len(active_user.workouts) + 1:
                        choice = ''
                        break
                    elif choice in ["q", "Q"]:
                        break
                    else:
                        workout_chosen = active_user.workouts[choice - 1]
                        while choice not in ["q", "Q"]:
                            choice = uiMenu(["Add exercise", "Delete Exercise", "Go back to weekly workouts menu"], menu_title="Exercises", sub_title="Exercises of this workout:", sub_sub_title=getattr(
                                workout_chosen, "printExercises"), user_instruction="What would you like to do?")
                            if choice == 1:
                                exercise_data = uiMenu(["Enter exercise"], menu_title="Add Exercise", input_type="questions", error_keys=[
                                                       "exercise"], questions_check_functions=[checkExerciseValid])
                                new_exercise = exercise(workout_chosen.workoutID, exercise_data[0])
                                workout_chosen.updateExercises()
                                active_user.updateWorkouts()
                            if choice == 2:
                                while choice not in ["q", "Q"]:
                                    choice = uiMenu(workout_chosen.exercises + [
                                                    "Go back to Exercises"], menu_title="Delete Exercises", user_instruction="Which exercise do you want to delete?:")
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
                while choice not in ["q", "Q"]:
                    choice = uiMenu(active_user.workouts + ["Go back to Fitness Menu"],
                                    menu_title="Weekly Workouts", user_instruction="Choose a workout to delete:")
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
                # Weight goal
                weight_goal = uiMenu(["Enter weight goal"], menu_title="Set weight goal", input_type="questions", error_keys=[
                                     "weight"], questions_check_functions=[checkWeight])
                userDao.setWeightGoal(active_user.userID, weight_goal)
                active_user.setWeightGoal()
                active_user.setCalorieNeed()
                active_user.setNetCalorieNeed()

            if choice == 5:
                while choice not in ["q", "Q"]:
                    # Mapping menu
                    # ["1 Find me a gym near me", "2 Find me a gym from another location", "3 Go back to main menu"]
                    choice = uiMenu(gymMenu, menu_title="Find a gym",
                                    user_instruction="Which option do you want?")
                    if choice == 1:
                        map = maps(active_user.address)
                        map.getLocation()
                        print("Your location is: " + str(map.location))
                        map.getNearbyPlace("gym")
                        choice = uiMenu(directionsMenu, menu_title="How to you want to reach your destination?",
                                        user_instruction="Which option do you want?")

                        if choice == 1:
                            map.mode = "walking"

                        if choice == 2:
                            map.mode = "driving"

                        if choice == 3:
                            map.mode = "transit"

                        if choice == 4:
                            choice = ""
                            break

                        map.getDistance()
                        map.getDirection()
                        map.getImg()
                        map.sendEmail(active_user.eMail)
                        time.sleep(5)
                        choice = ""
                        break

                    if choice == 2:
                        address = input("For which address would you like find a gym? :")
                        map = maps(address)
                        map.getLocation()
                        print("Your location is: " + str(map.location))
                        map.getNearbyPlace("gym")
                        choice = uiMenu(directionsMenu, menu_title="How to you want to reach your destination?",
                                        user_instruction="Which option do you want?")

                        if choice == 1:
                            map.mode = "walking"

                        if choice == 2:
                            map.mode = "driving"

                        if choice == 3:
                            map.mode = "transit"

                        if choice == 4:
                            choice = ""
                            break

                        map.getDistance()
                        map.getDirection()
                        map.getImg()
                        map.sendEmail(active_user.eMail)
                        time.sleep(5)
                        choice = ""
                        break

                    if choice == 3:
                        break

            if choice == 6:
                choice = ''
                # Go back to main menu
                break
    if choice == 4:
        while choice not in ["q", "Q"]:
            # Shopping
            # ["Find the nearest supermarket", "Get my shopping list", "Check price development", "Go back to main menu"]
            choice = uiMenu(shoppingMenu, menu_title="Shopping",
                            user_instruction="What would you like to do?")
            if choice == 1:
                while choice not in ["q", "Q"]:
                    # ["Find me a supermarket near me", "Find me a supermarket from another location", "Go back to previous menu"]
                    choice = uiMenu(supermarketMenu, menu_title="Find a supermarket",
                                    user_instruction="Which option do you want?")
                    if choice == 1:
                        map = maps(active_user.address)
                        map.getLocation()
                        print("Your location is: " + str(map.location))
                        map.getNearbyPlace("supermarket")
                        choice = uiMenu(directionsMenu, menu_title="How to you want to reach your destination?",
                                        user_instruction="Which option do you want?")

                        if choice == 1:
                            map.mode = "walking"

                        if choice == 2:
                            map.mode = "driving"

                        if choice == 3:
                            map.mode = "transit"

                        if choice == 4:
                            choice = ""
                            break

                        map.getDistance()
                        map.getDirection()
                        map.getImg()
                        map.sendEmail(active_user.eMail)
                        time.sleep(5)
                        choice = ""
                        break

                    if choice == 2:
                        address = input("For which address would you like find supermarkets? :")
                        map = maps(address)
                        map.getLocation()
                        print("Your location is: " + str(map.location))
                        map.getNearbyPlace("supermarket")
                        choice = uiMenu(directionsMenu, menu_title="How to you want to reach your destination?",
                                        user_instruction="Which option do you want?")

                        if choice == 1:
                            map.mode = "walking"

                        if choice == 2:
                            map.mode = "driving"

                        if choice == 3:
                            map.mode = "transit"

                        if choice == 4:
                            choice = ""
                            break

                        map.getDistance()
                        map.getDirection()
                        map.getImg()
                        map.sendEmail(active_user.eMail)
                        time.sleep(5)
                        choice = ""
                        break

                    if choice == 3:
                        break
            # Make shopping list for a favourite recipe.
            if choice == 2:
                active_user.setFavRecipes()
                while choice not in ["q", "Q"]:
                    choice = uiMenu(active_user.favrecipeshort + ["Go back to previous Menu"], menu_title="Shopping List",
                                   user_instruction="For which receipe do you want a shopping list?")

                    choice_recipe = choice
                    if choice == len(active_user.favrecipeshort) + 1:
                       choice = ''
                       break

                    if choice in ["q", "Q"]:
                        break

                    else:
                        #recipe_chosen = active_user.favrecipeshort[choice - 1]
                        #recipe_chosen_index = int(choice)-int(1)
                        while choice not in ["q", "Q"]:

                            recipe_chosen = active_user.favrecipeshort[choice_recipe - 1]
                            recipe_chosen_index = int(choice_recipe)-int(1)

                            choice = uiMenu(["See the shopping list", "Send me the shopping list", "Go back to different recipes"],
                                            menu_title="Shopping List", sub_title=recipe_chosen, user_instruction="What would you like to do?")

                            if choice == 1:
                                # Shopping list

                                new_shoppingList = shoppinglist(recipe_chosen_index, active_user.userID)
                                choice = uiMenu(
                                    ["Send shopping list to email", "Go back to shooping lists"],
                                    menu_title="Shopping List", sub_title=new_shoppingList.getShoppingListAsString(),
                                    user_instruction="What would you like to do?")
                                if choice == 1:
                                    choice = ""
                                    new_shoppingList.sendEmail(active_user.eMail)
                                    break

                                if choice == 2:
                                    choice = ""
                                    break

                            if choice == 2:
                                while choice not in ["q", "Q"]:
                                    choice = ""
                                    new_shoppingList = shoppinglist(recipe_chosen_index, active_user.userID)
                                    new_shoppingList.sendEmail(active_user.eMail)
                                    break

                            if choice == 3:
                                choice = ""
                                break
            if choice == 3:
                choice = ""
                break

    if choice == 5:
        while True:
            choice = uiMenu(active_user.familyMembers + ["Add Family Member", "Go back to Main Menu"],
                            menu_title="Family Members", user_instruction="Choose a family member to delete or another option:")
            if choice == len(active_user.familyMembers) + 2:
                choice = ''
                break
            elif choice in ["q", "Q"]:
                break
            elif choice == len(active_user.familyMembers) + 1:
                # Add Family Member
                family_member_username = uiMenu(["Enter username of family member"], menu_title="Add Family Member", input_type="questions", error_keys=[
                                                "username"], questions_check_functions=[checkFamilyMember], questions_check_functions_additional_args=[[active_user.username, active_user.familyMembersUsernames]])
                userDao.addFamilyMember(active_user.userID, family_member_username)
                active_user.setFamilyMembers()
            else:
                # Delete Family Member
                userDao.deleteFamilyMember(
                    active_user.userID, active_user.familyMembers[choice - 1].userID)
                active_user.setFamilyMembers()
    if choice == 6:
        # Food Log
        while choice not in ["q", "Q"]:
            choice = uiMenu(["Add food", "Go back to main menu"],
                            menu_title="Food Log", user_instruction="What would you like to do?")
            if choice == 1:
                food = uiMenu(["Enter food"], menu_title="Food Log", input_type="questions", error_keys=[
                              "food"], questions_check_functions=[apiFoodNutritions.checkFoodInApi])
                foodLogDao.setMeal(food, apiFoodNutritions.getCaloriesOfFood(
                    food[0]), active_user.userID)
                active_user.setTodaysCaloricIntake()
                active_user.setNetCalorieNeed()
            if choice == 2:
                choice = ''
                break
    if choice == 7:
        # Logout
        while choice not in ["q", "Q"]:
            choice = uiMenu(logInMenu, menu_title="Login",
                            user_instruction="What would you like to do?")
            if choice == 1:
                username = uiMenu(["Username"], menu_title="Login", error_keys=["username"],
                                  input_type="questions", questions_check_functions=[userDao.checkUsernameExists])
                uiMenu(["Password"], menu_title="Login", error_keys=["password"],
                       input_type="questions", questions_check_functions=[userDao.checkValidPassword], questions_check_functions_additional_args=[username], questions_special_input_func=[getpass])
                active_user = user.from_username(username)
                break
            if choice == 2:
                user_data = uiMenu(
                createUserProfil,
                menu_title="Create User Profile",
                error_keys=[
                "name",
                None,
                "name",
                "gender",
                "height",
                "weight",
                "email",
                "birth",
                "address",
                "diet",
                "intolerance",
                "username",
                "password"],
                input_type="questions",
                questions_check_functions=[
                checkIfStringLenNeqZero,
                None,
                checkIfStringLenNeqZero,
                checkGender,
                checkHeight,
                checkWeight,
                checkEmail,
                checkValidYearOfBirth,
                checkAddress,
                checkDiet,
                checkIntolerances,
                checkNewUsername,
                checkIfStringLenNeqZero],
                questions_special_input_func=[None, None, None, None,
                                          None, None, None, None, None, None, None, None, getpass]
                )
                active_user = user.from_list(user_data)
                break


# Show Quit
showQuit()
