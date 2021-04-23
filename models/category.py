
from models.entity import Entity
from utils.manager import Manager


class Category(Entity):
    table = "category"
    name = None

    def __init__(self, name):
        self.name = name.replace("'", " ")

    def __str__(self):
        return f"catégorie: {self.name}"


Category.objects = Manager(Category)