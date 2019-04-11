# gets a choice input
def getChoiceInput(user_input):
    if user_input not in ["q", "Q"]:
        return int(user_input)
    else:
        return user_input

def getErrorMessage(error_code, custom_message = ''):
    errorMessages = {
    "choice" : "\nError! Please enter a valid option:"
    }
    return errorMessages[error_code]