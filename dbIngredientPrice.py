import migros_prices as migros
import dbFunctions




#products = ["Knoblauch", "Zwieblen", "Tomaten", "Karotten", "Kopfsalat", "Peperoni", "Valflora Halbrahm", "M-Classic Rindshackfleisch"]


products = ["Valflora Halbrahm", "Knoblauch"]
# Loop through the products with the respective functions and save the returned lists!
for product in products:

    print(f"One moment please. Trying to get the price for {product}...")
    scraper = migros.MigrosScraper(product)
    scraper.load_Migros_url()

    # Save the three lists
    brand = scraper.extract_product_brand()
    name = scraper.extract_product_name()
    price = scraper.extract_product_price()

    scraper.quit()


    DBEntry = []

    for i in range(len(brand)):
        if (brand[i] == "Fresh product" and ((len(name[i])-len(product)) <= 6)) or (name[i] in product):

            DBEntry.append(brand[i] + "," + name[i].replace(",", "-") + "," + price[i])

    print(DBEntry)

    dbFunctions.addnewMigrosPrice(product, DBEntry)