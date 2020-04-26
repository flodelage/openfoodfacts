import requests
import mysql.connector
import json


db = mysql.connector.connect(
  host = "localhost",
  database = 'openfoodfacts',
  user = "root",
  passwd = ""
)

request = requests.get("https://fr.openfoodfacts.org/categorie/pates-a-tartiner-aux-noisettes-et-au-cacao.json")
result = request.json()

"""
serializeddata = json.dumps(result)
file = open("data.json", "w")
file.write(serializeddata)
file.close()
"""

"""
data.keys() --> dict_keys(['count', 'products', 'skip', 'page_size', 'page'])
type(data["products"]) --> <class 'list'>
type(data["products"][0]) --> <class 'dict'>
"""


"""
first_product = data["products"][1]
print( f"product_name: {first_product['product_name']}" )
print( f"brands: {first_product['brands']}" )
print( f"nutrition_grade_fr: {first_product['nutrition_grade_fr']}" )
print( f"stores: {first_product['stores']}" )
print( f"url: {first_product['url']}" )
"""
"""
mycursor = db.cursor()

sql = "INSERT INTO product (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

db.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
"""
print(result["count"], result["page_size"])
for product in result["products"]:
    try:
        print(product['product_name'])
    except:
        pass

    try:
        print(product['brands'])
    except:
        pass

    try:
        print(product['nutrition_grade_fr'])
    except:
        pass

    try:
        print(product['nutriscore_score'])
    except:
        pass

    try:
        print(product['stores'])
    except:
        pass

    try:
        print(product['url'])
    except:
        pass

    try:
        print(product['categories'])
    except:
        pass

    print("______________________________________________")


