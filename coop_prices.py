from bs4 import BeautifulSoup as soup
import requests


class CoopScraper(object):
    def __init__(self, product):
        self.query = product
        self.url = f"https://www.coopathome.ch/de/search/?text={self.query}"

    def loadCoopWebsite(self):
        source = requests.get(self.url).text
        return source

    def extractProductInfo(self, source):
        file_soup = soup(source, "lxml")

        product_name_list = []
        product_price_list = []
        product_weight_list = []

        for product in file_soup.findAll("li", class_="list-page__item"):

            try:
                product_name = product.find("div", class_="product-item__details").a.text.strip()
                info = product.find(
                    "dd", class_="product-item__price__value product-item__price__value--weight").findAll("span")
                product_weight = info[2].text.strip()
                product_price = info[3].text

                if "/100g" in product_price:
                    product_price = product_price.split("/")[0]
                    product_price = float(product_price)*10
                    product_price = format(product_price, ".2f")
                    product_price = str(product_price) + " / kg"

                product_name_list.append(product_name)
                product_weight_list.append(product_weight)
                product_price_list.append(product_price)
            except AttributeError:
                pass

        return product_name_list, product_weight_list, product_price_list


# # Loop through the products with the respective functions and save the returned lists!
# products = ["Chips", "Hackfleisch", "Milch", "Butter"]
#
# for product in products:
#     scraper = CoopScraper(product)
#
#     source = scraper.loadCoopWebsite()
#     # Save the three lists
#     name, weight, price = scraper.extractProductInfo(source)
#
#     # Create a csv file with the output added together!
#     filename = "Coop " + product + ".csv"
#     headers = "sep=,\nproduct, weight, price\n"
#     f = open(filename, "w")
#     f.write(headers)
#
#     for i in range(len(name)):
#         f.write(name[i].replace(",", "-") + "," + weight[i] + "," + price[i] + "\n")
#
#     f.close()
