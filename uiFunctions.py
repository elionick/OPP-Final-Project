import os
from designElements import *
from checkFunctions import *
from getFunctions import *
from menuElements import *

# displays a menu and returns an input
def uiMenu(menu_elements_list, menu_title = None, user_instruction = None,  nOptions = None, header = "logo", input_type = "choice", error_keys = ["choice"], clear = True, quit_option = True, initial_error = False, questions_check_functions = None):
    error_status = initial_error
    if input_type == "questions":
        answers = []
    design_elements = {
        'logo' : showLogo,
        'welcome' : showWelcome,
        'quit' : showQuit
    }
    while True:
        if clear == True:
            os.system('clear')
        if header == "logo":
            design_elements[header]()
        print("")
        if menu_title != None:
            print("*** " + menu_title + " ***")
        print("")
        if input_type == "choice":
            for index, element in enumerate(menu_elements_list):
                print(str(index + 1) + ": " + element)
            if quit_option == True:
                print("q: Quit")
            print("")
            if user_instruction != None:
                print(user_instruction)
            if error_status == True:
                print(getErrorMessage(error_keys[0]))
                print("")
            user_input = input()
            if nOptions == None:
                nOptions = len(menu_elements_list)
            if checkIfChoice(user_input, range(1, nOptions), quit_option = quit_option)  == False:
                error_status = True
            else:
                choice = getChoiceInput(user_input)
                return choice
        if input_type == "questions":
            for index, answer in enumerate(answers):
                print(menu_elements_list[index] + ": " + answer)
                print("")
            if error_status == True:
                print(getErrorMessage(error_keys[len(answers)]))
            user_input = input(menu_elements_list[len(answers)] + ": ")
            if questions_check_functions != None:
                if questions_check_functions[len(answers)] != None:
                    if questions_check_functions[len(answers)](user_input) == False:
                        error_status = True
                    else:
                        answers.append(user_input)
                        if len(menu_elements_list) == len(answers):
                            return answers
                else:
                    answers.append(user_input)
                    if len(menu_elements_list) == len(answers):
                        return answers


                


        

if __name__ == "__main__":
#    displayMenu(["Recipes", "Fitness", "Shopping"], menu_title = "Main Menu")
#    displayMenu(["Recipes", "Fitness", "Shopping"], menu_title = "Main Menu", user_instruction="What would you like to do?")
#    displayMenu(["Recipes", "Fitness", "Shopping"], menu_title = "Main Menu", quit_option = False, user_instruction="What would you like to do?")
    displayMenu(createUserProfil, menu_title = "Create User Profile", error_keys = [None, "age"], input_type="questions", questions_check_functions = [None, checkIfAge])