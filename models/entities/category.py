
import unidecode
from models.manager import Manager


class Category():
    table = "category"
    name = None

    def __init__(self, name):
        self.objects = Manager()
        self.name = name.replace("'", " ")

    def get_name(self):
        return self.name

    def save(self):
        from database import Database
        db = Database()
        db.save(self)