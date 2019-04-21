import migros_prices as migros
import dbFunctions

# List with some of the most commonly used ingredients, which we are pre-saving!


products = ["Zwieblen", "Knoblauch", "Karotten", "Peperoni", "Tomaten",
            "Kopfsalat", "Valflora Halbrahm", "M-Classic Rindshackfleisch"]

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

    # Prepare the data which will be sent to the DB!
    DBEntry = []
    for i in range(len(brand)):
        # Only include the most relevant entries
        if (brand[i] == "Fresh product" and ((len(name[i])-len(product)) <= 6)) or (name[i] in product):

            DBEntry.append(brand[i] + "," + name[i].replace(",", "-") + "," + price[i])

    # Clean and standardize the table_names
    if brand[0] in product:
        tablename = name[0] + "_PRICE"
        tablename = tablename.upper()

    else:
        tablename = product + "_PRICE"

    # Check if the table is already created, and if yes, enter the values
    if dbFunctions.checkTableExist(tablename) is True:
        dbFunctions.addnewMigrosPrice(tablename, DBEntry)

    # If the table does not exist, create one and enter the values
    else:
        dbFunctions.createNewPriceTable(tablename, "ENTRY_ID", "BRAND", "PRODUCT", "PRICE", "DATE")
        dbFunctions.addnewMigrosPrice(tablename, DBEntry)
