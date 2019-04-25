import coop_prices as coop

# Loop through the products with the respective functions and save the returned lists!
products = ["Chips"]
coop_brands = ["Naturaplan", "Bio", "Prix", "Garantie", "Naturafarm", "Emmi", "Floralp", "Zweifel"]
for product in products:
    scraper = coop.CoopScraper(product)

    source = scraper.loadCoopWebsite()
    # Save the three lists
    name, weight, price = scraper.extractProductInfo(source)

    DBEntry = []
    brand = []

    # Separate the brand out of the name
    for i in range(len(name)):
        name_splited = ""
        for coop_brand in coop_brands:
            if coop_brand in name[i]:
                name_splited = name[i].split(" ")
        brand_string = []
        counter = 0
        for substring in name_splited:
            if substring in coop_brands:
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

        DBEntry.append(brand[i] + "," + name[i] + "," + price[i])


#
    print(DBEntry)
#
