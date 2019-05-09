from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


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
            print(self.product + " Page is ready!")
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
            if product.text == "":
                brand = "Fresh product"
            else:
                brand = product.text
            product_brand_list.append(brand)
        return product_brand_list

    def extract_product_price(self):
        all_products = self.driver.find_elements_by_class_name("listMode-priceUnit")
        all_products_prices = self.driver.find_elements_by_class_name("listMode-price")
        product_price_list = []
        product_price_list_2 = []

        for product in all_products:
            product_price_list.append(product.text)

        for product in all_products_prices:
            price = product.text.replace("\n", " ")
            product_price_list_2.append(price)

        for i in range(len(product_price_list)):
            if product_price_list[i] == "":
                product_price_list[i] = product_price_list_2[i]

        return product_price_list

    def quit(self):
        self.driver.close()
