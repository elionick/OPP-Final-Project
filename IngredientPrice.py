
# WORK IN PROGRESS
class priceGetter:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def findIngredients(self):
        splitIngredients = []
        foods = ["onion", "tomatoes", "beef"]
        for i in range(len(self.ingredients)):
            splitIngredients.append(self.ingredients[i].split(" "))

        finalIngredients = []
        for i in range(len(splitIngredients)):
            for n in range(len(splitIngredients[i])):
                if splitIngredients[i][n] in foods:
                    finalIngredients.append(splitIngredients[i][n])
                else:
                    print(splitIngredients[i][n] + " is NOT an ingredient!")

        print("Final ingredients: " +str(finalIngredients))

ingre = ["small onion", "2 tomatoes", "500g beef"]
test = priceGetter(ingre)
test.findIngredients()

