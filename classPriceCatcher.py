import classCoopPrices as coop
import translateFunctions
import apiFoodNutritions as food
import re


class priceRetriever:

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.finalIngredients = []
        self.IngredientPrices = []
        self.finalIngredientsGerman = []

    def filterIngredients(self):
        irrelevant_measurements = ["Tbsps", "tsp", "Tbs", "teaspoon", "Tbsp", "tablespoon", "Tablespoon"]
        for each in irrelevant_measurements:
            for i in range(len(self.ingredients)):
                if each in self.ingredients[i]:
                    self.ingredients[i] = "irrelevant measurement"
        try:
            for i in range(len(self.ingredients)):
                self.ingredients.remove('irrelevant measurement')
        except ValueError:
            pass

    def findIngredients(self):

        splitIngredients = []
        for i in range(len(self.ingredients)):
            splitIngredients.append(self.ingredients[i].split(" "))

        print("Checking for ingredients...")
        # Check with the API which string is food
        for i in range(len(splitIngredients)):
            for n in range(len(splitIngredients[i])):
                tester = food.apiFoodNutritions()
                if tester.checkFoodInApi(splitIngredients[i][n]):
                    self.finalIngredients.append(splitIngredients[i][n])
                    break

    def translateIngredients(self):
        for i in range(len(self.finalIngredients)):
            self.finalIngredientsGerman.append(
                translateFunctions.translate(self.finalIngredients[i]))

    def getCoopPrices(self):

        brandsCoop = ["Naturaplan", "Bio", "Prix", "Garantie",
                      "Naturafarm", "Emmi", "Floralp", "Zweifel"]

        for ingredient in self.finalIngredientsGerman:

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
            # Check if we could find the good
            if name == []:
                print("We could not get prices for " + str(ingredient))
                self.IngredientPrices.append(str(0) + "," + str(0) + "," + str(0.00))

            else:
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
                # self.IngredientPricesonly.append(price[n])


if __name__ == "__main__":
    pass
    # ingredients = ['2.0 Tbsps barbeque sauce', '1.0 tsp ground cayenne pepper', '566.99 g ground turkey breast', '5.0  split hamburger buns', '84.75 ml honey',
    #                '1.0 Tbsp cooked horseradish', '1.0  jalapeno pepper', '224.0 ml light mayonnaise', '0.25 tsps liquid smoke', '5.0 servings sweet mayo', '62.25 ml mustard', '1.0 Tbsp olive oil']
    # test = priceRetriever(ingredients)
    # print(test.ingredients)
    # test.filterIngredients()
    # print(test.ingredients)
    # # test.findIngredients()
    # test.finalIngredients = ['turkey', 'hamburger', 'honey',
    #                          'jalapeno', 'mayonnaise', 'mayo', 'mustard']
    # print(test.finalIngredients)
    # print("----------")
    #
    # test.translateIngredients()
    # print(test.finalIngredients)
    # print(test.finalIngredientsGerman)
    # print("----------")
    #
    # test.getCoopPrices()
    # print(test.IngredientPrices)
    #
    # price_list = []
    # # IngredientPrices = ['Coop,Avocado 1 St�ck,2.3', 'Bio,Karma Betty Bossi  Tofu B�rlauch,24.8',
    # #                     'Coop,Curry mild,21.0', 'Coop,Eichblatt-Salat gr�n 1 St�ck,2.6']
    # #
    # adjustedprices = []
    # #
    #
    # for i in range(len(ingredients)):
    #     r = re.compile(r'\d*\s*g|\d*.\d*\s*ml')
    #     matches = r.findall(ingredients[i])
    #     for match in matches:
    #         adjustedprices.append([i, str(match).split("g")[0].split("ml")[0].strip()])
    #
    #     # index = int(adjustedprices[0][0])
    #     # print(price_list[index])
    # # print(adjustprices)
    # #
    # # for n in range(len(adjustprices)):
    # #     print(IngredientPrices[adjustprices[n][0]])
    # #
    # i = 0
    # while i < len(test.IngredientPrices):
    #     test1 = test.IngredientPrices[i]
    #     test1 = test1.split(",")
    #     # print(test1[2])
    #     price_list.append(float(test1[2]))
    #     i += 1
    # print(price_list)
    # for i in range(len(adjustedprices)):
    #     if price_list[adjustedprices[i][0]] > 10:
    #         price_list[adjustedprices[i][0]] = float(
    #             price_list[adjustedprices[i][0]]) / float((1000/float(adjustedprices[i][1])))
    #
    # print(price_list)
    # # index = int(adjustedprices[0][0])
    # # print(price_list[index])
    # # print(adjustedprices)
    # #
    # # for n in range(len(adjustprices)):
    # #     print(IngredientPrices[adjustprices[n][0]])
    # #
    # price = "%.2f" % sum(price_list)
    # print("Approximate Price for that recipe: " + str(price) + " CHF")
