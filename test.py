product = "Halbrahm"

sql = "INSERT INTO " + product + " (brand, product, price, date) VALUES (%s, %s, %s, %s)"

print(sql)
