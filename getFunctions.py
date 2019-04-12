# gets a choice input
def getChoiceInput(user_input):
    if user_input not in ["q", "Q"]:
        return int(user_input)
    else:
        return user_input

def getErrorMessage(error_code, custom_message = ''):
    errorMessages = {
    "choice" : "Error! Please enter a valid option.",
    "age" : "Error! Please enter a valid age (1-99)."
    }
    return errorMessages[error_code]