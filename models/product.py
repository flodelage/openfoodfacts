
import unidecode
from models.entity import Entity
from models.category import Category
from utils.manager import Manager


class Product(Entity):
    table = "product"
    brand = None
    name = None
    nutrition_grade = None
    stores = None
    url = None
    category = []

    def __init__(self, brand, name, nutrition_grade, stores, url, category=None): # must be sorted in alphabetical order, and list in the end
        self.name = name
        self.brand = brand
        self.nutrition_grade = nutrition_grade
        self.stores = stores
        self.url = url
        self.category = category
        if type(category) is str:
            self.category = []
            for cat in category.split(","):
                self.category.append(Category(name=cat))

    def __str__(self):
        return f"*** {self.name} ***\n Marque: {self.brand}, Nutriscore: {self.nutrition_grade.capitalize()}, Magasins: {self.stores}, Lien: {self.url}"


Product.objects = Manager(Product)