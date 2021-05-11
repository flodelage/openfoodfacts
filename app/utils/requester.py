
import requests
import unidecode

from app.settings import CATEGORIES, DB_NAME
from app.models.product import Product
from app.utils.manager import Manager


class Requester:
    """
    Calls the API in order to retrieve the necessary data
    then create products and categories instances
    """
    def __init__(self):
        self.manager = Manager(self)

    def url_to_json(self, category_name):
        """
        send a get request to the API in order to
        return the json concerning a specific category
        """
        request = requests.get(f"https://fr.openfoodfacts.org/categorie/{category_name}.json")
        return request.json()

    def page_to_json(self, category_name, page):
        """
        send a get request to the API in order to
        return the json concerning a specific category page
        """
        request = requests.get(f"https://fr.openfoodfacts.org/categorie/{category_name}/{page}.json")
        return request.json()

    def retrieve_cat_pages_nb(self, json_data):
        """
        Determines the nb of pages in the API affected by a category by
        dividing the nb of total products by the nb of products per page.
        Then returns the number rounded to the next whole number
        """
        return round(int(json_data["count"]) / json_data["page_size"]) + 1

    def clean_data(self, objects_list):
        """
        Sort a list of products so that none have the same name.
        This avoid SQL errors due to duplications while
        capital letters or accents make them different.
        Example: for MySql, Nutella and nutella are identical /
        Jambon fumé and Jambon fume are identical
        """
        cleaned_list = []
        names = []
        for obj in objects_list:
            name = unidecode.unidecode(obj.name.strip().lower())
            if name not in names:
                cleaned_list.append(obj)
                names.append(name)
        return cleaned_list

    def get_data(self):
        """
        Retrieves and processes data from the API.
        Create the objects.
        Then inserts them into the database
        by calling the Manager.save_all() method.
        """
        products_list = []
        for category in CATEGORIES:
            json_data = self.url_to_json(category)
            pages_nb = self.retrieve_cat_pages_nb(json_data)
            for page in range(pages_nb):
                page_json_data = self.page_to_json(category, page+1)
                products = page_json_data["products"]
                for p in products:
                    params = {
                        'brands': "",
                        'product_name_fr': "",
                        'nutrition_grades': "",
                        'stores': "",
                        'url': "",
                        'categories': ""
                    }
                    for key in params:
                        try:
                            params[key] = p[key]
                        except KeyError:
                            continue
                    if params['product_name_fr'] != "" and params['nutrition_grades'] != "" and params['url'] != "" and params['categories'] != "":
                        product = Product(brand=params['brands'],
                                          name=params['product_name_fr'],
                                          nutrition_grade=params['nutrition_grades'],
                                          stores=params['stores'], url=params['url'],
                                          category=params['categories'])
                        products_list.append(product)
        try:
            self.manager.save_all(self.clean_data(products_list))
            print(f"\n La base de données |{DB_NAME}| a été peuplée \n")
        except:
            print("\n Une erreur s'est produite lors "
                  "du peuplement de la base de données \n")
