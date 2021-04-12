
from models.entities.entity import Entity
from models.entities.product import Product
from models.manager import Manager

class Substitute(Entity):
    table = "substitute"
    product = None
    substitute = None

    def __init__(self, product=None, substitute=None):
        self.product = product
        self.substitute = substitute


Substitute.objects = Manager(Substitute)