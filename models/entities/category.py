
import unidecode
import inspect
from models.manager import Manager


class Category():
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

    @classmethod
    def params(cls):
        attributes = inspect.getmembers(cls, lambda attr:not(inspect.isroutine(attr)))
        filtered_attributes = dict( [attr for attr in attributes if not(attr[0].startswith('__') and attr[0].endswith('__'))] )
        return {
            key: value
            for key, value in filtered_attributes.items()
            if value is None or (isinstance(value, list) == True)
        }

Category.objects = Manager(Category)