
import requests
import json
from settings import CATEGORIES, DB_NAME
from database import Database
from models.product import Product
from models.category import Category


class Requester:
    def __init__(self):
        self.db = Database()

    def url_to_json(self, category_name):
        request = requests.get(f"https://fr.openfoodfacts.org/categorie/{category_name}.json")
        return request.json()

    def page_to_json(self, category_name, page):
        request = requests.get(f"https://fr.openfoodfacts.org/categorie/{category_name}/{page}.json")
        return request.json()

    def retrieve_cat_pages_nb(self, json_data):
        return round(int(json_data["count"]) / json_data["page_size"])

    def get_data(self):
        products_list = []
        categories_list = []
        for category in CATEGORIES:
            json_data = self.url_to_json(category) # store json from category url
            pages_nb = self.retrieve_cat_pages_nb(json_data) # store the number of pages the category

            for page in range(pages_nb+1):
                json_data = self.page_to_json(category, page) # store the current page of the category
                products = json_data["products"] # store the products of the current page

                for p in products:
                    try:
                        product = Product(name=p['product_name'], brand=p['brands'], nutrition_grade=p['nutrition_grades'], stores=p['stores'], url=p['url'])
                        products_list.append(product)
                    except:
                        continue

                    for cat in p['categories'].split(","):
                        category = Category(name=cat)
                        categories_list.append(category)

        return products_list, categories_list

    def clean_data(self):
        categories = self.get_data()[1]
        cleaned_categories = []
        categories_name = []

        for cat in categories:
            if cat.get_name() not in categories_name:
                cleaned_categories.append(cat)
                categories_name = [cat.get_name() for cat in cleaned_categories]




    def insert_data(self):
        data_to_insert = self.get_data()
        for data in data_to_insert:
            self.db.save_all(data)

r = Requester()
r.clear_data()
