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

def checkStringIsInt(input):
    try: 
        if input.isdigit() == True:
            return True
        else:
            return False
    except ValueError:
        return False

def checkIfAge(input):
    if checkStringIsInt(input) == True:
        input = int(input)
        if input > 0 and input < 100:
            return True
        else:
            return False
    else:
        return False
        