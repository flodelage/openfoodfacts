
from models.entities.entity import Entity
from models.entities.product import Product
from models.manager import Manager

class Substitute(Entity):
    table = "substitute"
    product = []

    def __init__(self, product=None):
        self.product = product
        if isinstance(self.product, Product):
            prod = self.product
            self.product = []
            self.product.append(prod)


Substitute.objects = Manager(Substitute)