
from models.category import Category


class Product:
    table = "product"
    name = None
    brand = None
    nutrition_grade = None
    stores = None
    url = None

    def __init__(self, name, brand, nutrition_grade, stores, url):
        self.name = name
        self.brand = brand
        self.nutrition_grade = nutrition_grade
        self.stores = stores
        self.url = url
        # self.categories_list = []
        # for cat in categories.split(","): # turn the categories string into list of categories
        #     self.categories_list.append(Category(name=cat)) # for each cat: append in categories_list an object Category

    def get_name(self):
        return self.name

    def get_brand(self):
        return self.brand

    def get_nutrition_grade(self):
        return self.nutrition_grade

    def get_stores(self):
        return self.stores

    def get_url(self):
        return self.url

    def save(self):
        from database import Database
        db = Database()
        db.save(self)


