from uiFunctions import *
import time
from designElements import *
from menuElements import *

# Show Welcome
showWelcome()
time.sleep(2)

# Initialize choice
choice = ''

# Main Menu
while choice not in ["q", "Q"]:
    choice = uiMenu(mainMenu, menu_title = "Main Menu", user_instruction="What would you like to do?")
    if choice == 1:
        user_data = uiMenu(createUserProfil, menu_title = "Create User Profile", error_keys = [None, "age"], input_type="questions", questions_check_functions = [None, checkIfAge])

# Show Quit
showQuit()