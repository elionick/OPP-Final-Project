from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os


class MigrosScraper(object):
    def __init__(self, product):
        self.product = product
        self.url = f"https://www.leshop.ch/de/search?query={self.product}"

        # Open a new connection. Alternatively use "webdriver.Firefox()"
        self.driver = webdriver.Firefox()
        self.delay = 4

    def load_Migros_url(self):
        # Navigate to the website of Migros
        self.driver.get(self.url)
        try:
            # Wait until the element which contains the products is loaded.
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(ec.presence_of_element_located((By.CLASS_NAME, "subcat")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too long!")

    def extract_product_name(self):
        all_products = self.driver.find_elements_by_class_name("desc")
        product_title_list = []
        for product in all_products:
            name = product.text.replace("\n", " ")
            product_title_list.append(name)
        return product_title_list

    def extract_product_brand(self):
        all_products = self.driver.find_elements_by_class_name("name")
        product_brand_list = []
        for product in all_products:
            product_brand_list.append(product.text)
        return product_brand_list

    def extract_product_price(self):
        all_products = self.driver.find_elements_by_class_name("listMode-priceUnit")
        product_price_list = []
        for product in all_products:
            product_price_list.append(product.text)
        return product_price_list

    def quit(self):
        self.driver.close()


# Set the working directory to where the file is located, so the csv are saved here:
# Source: https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


# Different products which prices we want!
products = ["Chips", "Hackfleisch", "Milch", "Butter"]

# Loop through the products with the respective functions and save the returned lists!
for product in products:
    scraper = MigrosScraper(product)
    scraper.load_Migros_url()

    # Save the three lists
    brand = scraper.extract_product_brand()
    name = scraper.extract_product_name()
    price = scraper.extract_product_price()

    scraper.quit()

    # Create a csv file with the output added together!
    filename = "Migros " + product + ".csv"
    headers = "sep=,\nbrand, name, price\n"
    f = open(filename, "w")
    f.write(headers)

    for i in range(len(brand)):
        f.write(brand[i] + "," + name[i].replace(",", "-") + "," + price[i] + "\n")

    f.close()
