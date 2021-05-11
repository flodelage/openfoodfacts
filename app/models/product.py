
from app.models.entity import Entity
from app.models.category import Category
from app.utils.manager import Manager


class Product(Entity):
    table = "product"
    brand = None
    name = None
    nutrition_grade = None
    stores = None
    url = None
    category = []

    def __init__(self, brand, name, nutrition_grade,
                 stores, url, category=None):
        # params must be sorted in alphabetical order, and list in the end
        self.name = name
        self.brand = brand
        self.nutrition_grade = nutrition_grade
        self.stores = stores
        self.url = url
        self.category = category

        #  Plit the string containing the product categories
        # then create the instances by adding them to the category attribute
        # which has become a list
        if type(category) is str:
            self.category = []
            for cat in category.split(","):
                self.category.append(Category(name=cat))

        if self.brand == "":
            self.brand = "Non renseigné"

        if self.stores == "":
            self.stores = "Non renseigné"

    def __str__(self):
        """
        Default string that returns the details of a product
        """
        return f"*** {self.name} ***\n" \
               f"Marque: {self.brand}, " \
               f"Nutriscore: {self.nutrition_grade.capitalize()}, " \
               f"Magasins: {self.stores}, Lien: {self.url}"


Product.objects = Manager(Product)
