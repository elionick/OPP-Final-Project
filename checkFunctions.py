# checks if user input is possible choice
def checkChoiceInput(user_input, poss_options, quit_option = True):
    if quit_option == True:
        if user_input not in ["q", "Q"]:
            try:
                int(user_input)
                if int(user_input) in poss_options:
                    return True
                else: 
                    return False
            except ValueError:
                return False
        else:
            return True
    else:
        try:
            int(user_input)
            if int(user_input) in poss_options:
                return True
            else: 
                return False
        except ValueError:
            return False
        