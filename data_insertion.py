
import mysql.connector
import json
import requests
from database import Database
from settings import DB_HOST, DB_NAME, DB_PASSWD, DB_USER, CATEGORIES
from requester import Requester

class DataInsertion:
    def __init__(self):
        self.db = Database(DB_HOST, DB_USER, DB_PASSWD)
        self.db.connection._database = DB_NAME
        self.req = Requester()

    def insert(self):
        for category in CATEGORIES:
            # store json from category url
            json_data = self.req.url_to_json(category)
            # store the number of pages the category has
            pages_nb = self.req.retrieve_cat_pages_nb(json_data)

            for page in range(pages_nb+1):
                json_data = self.req.page_to_json(category, page)
                products = json_data["products"]
                
                for p in products:
                    try:
                        query = f"INSERT INTO product (name, brand, nutrition_grade, stores, url) VALUES (%s, %s, %s, %s, %s)"
                        values = (p['product_name'], p['brands'], p['nutrition_grades'], p['stores'], p['url'])
                        self.db.cursor.execute(query, values)
                        self.db.connection.commit()
                    
                        categories = p['categories'].split(", ")
                        for cat in categories:
                            try:
                                query = f"INSERT INTO category (name) VALUES ('{cat}')"
                                self.db.cursor.execute(query)
                                self.db.connection.commit()
                            except:
                                continue
                    except:
                        continue