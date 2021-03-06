import datetime
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
    "birth" : "Error! Please enter a valid birthday (format: yyyy-mm-dd).",
    "address": "Error! Please enter a valid address.",
    "username" : "Error! Please enter a valid username.",
    "password" : "Error! Please enter a valid password.",
    "diet" : "Error! Please enter a valid diet.",
    "intolerance" : "Error! Please enter a valid intolerance(s).",
    "gender": "Error! Please enter a valid gender.",
    "day": "Error! Please enter a valid day.",
    "time": "Error! Please enter a valid time.",
    "exercise": "Error! Please enter a valid exercise.",
    "food" : "Error! Please enter valid food."
    }
    return errorMessages[error_code]

def getTimeAsStringFromTimedelta(timedelta):
    days, seconds = timedelta.days, timedelta.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    if minutes < 10:
        retv = '{}:0{}'.format(hours, minutes)
    else:
        retv = '{}:{}'.format(hours, minutes)
    return retv

def getWeekdayNumber(weekday):
    weekdays_order = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return weekdays_order.index(weekday)

if __name__ == "__main__":
    pass