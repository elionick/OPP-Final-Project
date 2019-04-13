# gets a choice input
def getChoiceInput(user_input):
    if user_input not in ["q", "Q"]:
        return int(user_input)
    else:
        return user_input

def getErrorMessage(error_code, custom_message = ''):
    errorMessages = {
    "choice" : "Error! Please enter a valid option.",
    "name" : "Error! Name needed.",
    "height" : "Error! Please enter a valid height in meter (1m - 2.5m).",
    "weight" : "Error! Please enter a valid weight (40kg - 350 kg).",
    "email" : "Error! Please enter a valid email.",
    "birth" : "Error! Please enter a valid birthday (format: dd.mm.yyyy"
    }
    return errorMessages[error_code]

if __name__ == "__main__":
    b = input('T: ')