
import mysql.connector
import json
import requests
from database import Database
from settings import DB_HOST, DB_NAME, DB_PASSWD, DB_USER

db = Database(DB_HOST, DB_USER, DB_PASSWD)
db.existing_db_connection(DB_NAME)

request = requests.get("https://fr.openfoodfacts.org/categorie/pates-a-tartiner-aux-noisettes-et-au-cacao.json")
data = request.json()
pages_nb = round(data["count"] / data["page_size"])
pages = range(pages_nb +1)

for page in pages:
    request = requests.get(f"https://fr.openfoodfacts.org/categorie/pates-a-tartiner-aux-noisettes-et-au-cacao/{page}.json")
    data = request.json()
    products = data["products"]

    for p in products:
            try:
                query = "INSERT INTO product (name, brand, nutrition_grade, stores, url) VALUES (%s, %s, %s, %s, %s)"
                values = (p['product_name'], p['brands'], p['nutrition_grades'], p['stores'], p['url'])
                self.cursor.execute(query, values)
                self.connection.commit()

                categories = p['categories'].split(", ")
                for cat in categories:
                    try:
                        query = f"INSERT INTO category (name) VALUES ('{cat}')"
                        self.cursor.execute(query)
                        self.connection.commit()
                    except:
                        continue
            except:
                continue


instance de DB

lire une url 
définir le nombre de page de l'url

pour chaque page de la catégorie
on définit les produits
pour chaque produit
on crée une instance de produit
pour chacune des catégories du produit on crée une instance

et on enregistre en bdd  





