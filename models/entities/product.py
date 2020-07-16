
import unidecode
from models.entities.category import Category
from models.manager import Manager


class Product():
    table = "product"
    name = None
    brand = None
    nutrition_grade = None
    stores = None
    url = None
    categories = []

    def __init__(self, name, brand, nutrition_grade, stores, url, categories):
        self.name = name
        self.brand = brand
        self.nutrition_grade = nutrition_grade
        self.stores = stores
        self.url = url
        self.categories = []
        for cat in categories.split(","): # on découpe la string pour récupérer chaque catégorie
            self.categories.append(Category(name=cat)) # pour chaque catégorie récupérée on crée une instance de Category

    def __str__(self):
        return f"*** {self.name} *** brand: {self.brand} nutriscore: {self.nutrition_grade} stores: {self.stores} url: {self.url}"

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

    def get_categories(self):
        return self.categories

    def save(self):
        manager = Manager(self)
        manager.save(self)

Product.objects = Manager(Product)