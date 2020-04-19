
import mysql.connector
import json
import requests


db = mysql.connector.connect(
  host = "localhost",
  database = 'openfoodfacts',
  user = "root",
  passwd = ""
)

request = requests.get("https://fr.openfoodfacts.org/categorie/pates-a-tartiner-aux-noisettes-et-au-cacao.json")
data = request.json()

mycursor = db.cursor()

products = data["products"]

for p in products:
    try:
        query = "INSERT INTO product (name, brand, nutrition_grade, stores, url) VALUES (%s, %s, %s, %s, %s)"
        val = (p['product_name'], p['brands'], p['nutrition_grade_fr'], p['stores'], p['url'])
        mycursor.execute(query, val)
        db.commit()
    except:
        pass
