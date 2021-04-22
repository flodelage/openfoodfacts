
from models.entities.entity import Entity
from models.manager import Manager


class Category(Entity):
    table = "category"
    name = None

    def __init__(self, name):
        self.name = name.replace("'", " ")

    def __str__(self):
        return f"catégorie: {self.name}"

    def get_name(self):
        return self.name

    def save(self):
        manager = Manager(self)
        manager.save(self)


Category.objects = Manager(Category)