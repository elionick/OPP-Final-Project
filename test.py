import re
from classUser import *
from  recipeDao import *

class test():
    def __init__(self, userID):
        self.userID = userID
        self.favrecipe = ""
        self.list = []

    def getFavRecipes(self):
        self.favrecipe = getRecipeList(self.userID)
        if self.favrecipe == ():
            print(None)
        else:
            print(self.favrecipe)
            list = []
            for each in self.favrecipe:
                self.list.append(str(each["RECIPE_ID"]) +" " + str(each["RECIPE_NAME"]))
            print("list: "+str(list))
            # self.list = list
            print("Self list: "+str(self.list))
            print(len(self.list))


if __name__ == "__main__":
    test = test(46)
    test.getFavRecipes()