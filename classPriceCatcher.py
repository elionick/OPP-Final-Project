import classFoodNutritionsDao as food
import classCoopPrices as coop
import translateFunctions


class priceRetriever:

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.finalIngredients = []
        self.IngredientPrices = []

    def findIngredients(self):

        splitIngredients = []
        for i in range(len(self.ingredients)):
            splitIngredients.append(self.ingredients[i].split(" "))

        print("Checking for ingredients...")
        # Check with the API which string is food
        for i in range(len(splitIngredients)):
            for n in range(len(splitIngredients[i])):
                tester = food.FoodNutritionsDao()
                if tester.checkFoodInApi(splitIngredients[i][n]):
                    self.finalIngredients.append(splitIngredients[i][n])

    def translateIngredients(self):
        for i in range(len(self.finalIngredients)):
            self.finalIngredients[i] = translateFunctions.translate(self.finalIngredients[i])

    def getCoopPrices(self):

        brandsCoop = ["Naturaplan", "Bio", "Prix", "Garantie",
                      "Naturafarm", "Emmi", "Floralp", "Zweifel"]

        for ingredient in self.finalIngredients:

            # Create a new instance of the Coop Scraper
            scraper = coop.CoopScraper(ingredient)
            source = scraper.loadCoopWebsite()

            # Save the three lists
            name, weight, price = scraper.extractProductInfo(source)

            # Take only the most relevent results:
            name = name[0:5]
            weight = weight[0:5]
            price = price[0:5]

            brand = []
            if name == []:
                print("We could not get prices for " + str(ingredient))

            # Separate the brand out of the product-name
            for i in range(len(name)):
                name_splited = ""
                for coop_brand in brandsCoop:
                    if coop_brand in name[i]:
                        name_splited = name[i].split(" ")
                brand_string = []
                counter = 0
                for substring in name_splited:
                    if substring in brandsCoop:
                        brand_string.append(substring)
                        counter += 1
                if counter == 0:
                    brand.append("Coop")
                else:
                    brand.append(" ".join(brand_string))

            # Check if the brand name is in the product name
            for i in range(len(brand)):
                if brand[i] in name[i]:
                    name[i] = name[i].replace(brand[i], "")

            # Get the cheapest item
            for i in range(len(price)):
                price[i] = price[i].split()[0]
                price[i] = price[i].split("/")[0]
                price[i] = round(float(price[i]), 2)

            cheapestprice = min(price)
            n = price.index(cheapestprice)

            # Save the result
            self.IngredientPrices.append(brand[n] + "," + name[n] + "," + str(price[n]))


if __name__ == "__main__":

    ingredients = ["5 eggs", "onion", "bread"]
    # Create a new instance of the class, the input will be the ingredients list
    test = priceRetriever(ingredients)

    # Checks which of the ingredients is a food item with the API
    test.findIngredients()
    print(test.finalIngredients)

    # Translate these ingredients
    test.translateIngredients()
    print(test.finalIngredients)

    # Get the cheapest product - The result will be in the instance variable "self.IngredientPrices"
    test.getCoopPrices()
    print(test.IngredientPrices)
