
import requests
import json
import unidecode

from settings import CATEGORIES
from models.entities.product import Product
from models.entities.category import Category
from models.manager import Manager


class Requester:
    def __init__(self):
        self.manager = Manager(self)

    def url_to_json(self, category_name):
        request = requests.get(f"https://fr.openfoodfacts.org/categorie/{category_name}.json")
        return request.json()

    def page_to_json(self, category_name, page):
        request = requests.get(f"https://fr.openfoodfacts.org/categorie/{category_name}/{page}.json")
        return request.json()

    def retrieve_cat_pages_nb(self, json_data):
        return round(int(json_data["count"]) / json_data["page_size"]) + 1

    def get_data(self):
        products_list = []
        for category in CATEGORIES:
            json_data = self.url_to_json(category) # store json from category url
            pages_nb = self.retrieve_cat_pages_nb(json_data) # store the number of pages for the category

            for page in range(pages_nb):
                page_json_data = self.page_to_json(category, page+1) # store the current page for the category
                products = page_json_data["products"] # store the products for the current page

                for p in products:
                    try:
                        product = Product(name=p['product_name'], brand=p['brands'], nutrition_grade=p['nutrition_grades'], stores=p['stores'], url=p['url'], category=p['categories'])
                        products_list.append(product)
                    except KeyError:
                        continue
        self.manager.save_all(self.clean_data(products_list))

    def clean_data(self, objects_list):
        cleaned_list = []
        names = []
        for obj in objects_list:
            if unidecode.unidecode(obj.get_name().strip().lower()) not in names:
                cleaned_list.append(obj)
                names = [unidecode.unidecode(obj.get_name().strip().lower()) for obj in cleaned_list]
        return cleaned_list
