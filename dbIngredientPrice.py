import migros_prices as migros
import coop_prices as coop
import dbFunctions


# List with some of the most commonly used ingredients, which we are pre-saving!
products_Migros = ["Zwiebeln", "Knoblauch", "Karotten", "Peperoni", "Tomaten",
                   "Kopfsalat", "Valflora Halbrahm", "M-Classic Rindshackfleisch"]


# Loop through the products with the respective functions and save the returned lists!
for product in products_Migros:

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
        dbFunctions.addNewPrice(tablename, DBEntry)

    # If the table does not exist, create one and enter the values
    else:
        dbFunctions.createNewPriceTable(tablename, "ENTRY_ID", "BRAND", "PRODUCT", "PRICE", "DATE")
dbFunctions.addNewPrice(tablename, DBEntry)


# Loop through the products with the respective functions and save the returned lists!
productsCoop = ["Zwiebeln", "Knoblauch", "Karotten", "Peperoni",
                "Kopfsalat", "Halbrahm UHT", "Rinds Hackfleisch"]


brandsCoop = ["Naturaplan", "Bio", "Prix", "Garantie", "Naturafarm", "Emmi", "Floralp", "Zweifel"]
for product in productsCoop:
    scraper = coop.CoopScraper(product)

    source = scraper.loadCoopWebsite()
    # Save the three lists
    name, weight, price = scraper.extractProductInfo(source)

    DBEntry = []
    brand = []

    # Separate the brand out of the name
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

        # Only include the most relevant entries
        if ((len(name[i])-len(product)) <= 15) or (name[i] in product):
            DBEntry.append(brand[i] + "," + name[i] + "," + price[i])

    print(DBEntry)
    # Clean and standardize the table_names
    if brand[0] in product:
        tablename = name[0] + "_PRICE_COOP"
        tablename = tablename.upper()

    else:
        tablename = product + "_PRICE_COOP"

    # Check if the table is already created, and if yes, enter the values
    if dbFunctions.checkTableExist(tablename) is True:
        dbFunctions.addNewPrice(tablename, DBEntry)

    # If the table does not exist, create one and enter the values
    else:
        dbFunctions.createNewPriceTable(
            tablename, "ENTRY_ID", "BRAND", "PRODUCT", "PRICE", "DATE")
        dbFunctions.addNewPrice(tablename, DBEntry)
