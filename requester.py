
import mysql.connector
import requests
from database import Database
from settings import DB_HOST, DB_USER, DB_PASSWD, DB_NAME


class Requester:
    def url_to_json(self, category_name):
        request = requests.get(f"https://fr.openfoodfacts.org/categorie/{category_name}.json")
        json_data = request.json()
        return json_data

    def page_to_json(self, category_name, page):
        request = requests.get(f"https://fr.openfoodfacts.org/categorie/{category_name}/{page}.json")
        json_data = request.json()
        return json_data

    def retrieve_cat_pages_nb(self, json_data):
        pages_nb = round(int(json_data["count"]) / json_data["page_size"])
        return pages_nb
