from classUser import *
import sendEmail
import time

class shoppinglist():

    def __init__(self, chosen_recipe, userID):
        self.chosen_recipe = chosen_recipe
        self.favrecipe = ""
        self.userID = userID
        self.shoppinglist = []
        self.type = "shoppinglist"



    def printShoppingList(self):

        self.favrecipe = getRecipeList(self.userID)
        list = self.favrecipe[self.chosen_recipe]["INGREDIENTS"].replace("', ", "\n").replace("'", "").replace("[", "").replace("]", "").split("\n")
        self.shoppinglist = list
        return(list)


    def sendEmail(self, email):
        sendEmail.sendEmail(self.type, email, self.shoppinglist)
        print("We sent you an email to " + str(email) +
              " with the shopping list!")
        time.sleep(2)

if __name__ == "__main__":
    pass