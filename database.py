
import mysql.connector
import requests
from models.product import Product
from models.category import Category

class Database:
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd

        self.connection = mysql.connector.connect(
        host = self.host,
        user = self.user,
        passwd = self.passwd
        )
    
        self.cursor = self.connection.cursor()

    def existence_db(self, db_name):
        existence_query = f"USE {db_name}"
        try:
            self.cursor.execute(existence_query)
            return True
        except:
            return False

    def create_db(self, db_name):
        existence_query = f"USE {db_name}"
        creation_query = f"CREATE DATABASE {db_name} CHARACTER SET 'utf8' "
        # if openfoodfacts already exists
        try:
            self.cursor.execute(existence_query)
            print(f"\n La base de données |{db_name}| existe déjà \n")
        # if openfoodfacts database doesn't exist
        except:
            # try to create database
            try:
                self.cursor.execute(creation_query)
        # check if openfoodfacts database has been created
                self.cursor.execute(existence_query)   
                print(f"\n La base de données |{db_name}| a bien été créée \n")    
        # if openfoodfacts database has not been created
            except:
                print(f"\n La base de données |{db_name}| n'a pas pu être créée \n")

    def drop_db(self, db_name):
        existence_query = f"USE {db_name}"
        drop_query = f"DROP DATABASE {db_name}"
        # try to drop database
        try:
            self.cursor.execute(drop_query)
            # check if openfoodfacts database still exists
            try:
                self.cursor.execute(existence_query)
                # if openfoodfacts database still exists
                print(f"\n La base de données |{db_name}| n'a pas été supprimée \n")
            except:
                # if openfoodfacts database no longer exists
                print(f"\n La base de données |{db_name}| a été supprimée \n")
        # database openfoodfacts can't be droped because it doesn't exists
        except mysql.connector.errors.DatabaseError:
            print(f"\n La base de données |{db_name}| n'a pas pu être supprimée car elle n'existe pas \n")

    def existing_db_connection(self, db_name):
        self.connection._database = db_name
    







    def data_insertion(self):
        self.connection._database = "openfoodfacts"

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