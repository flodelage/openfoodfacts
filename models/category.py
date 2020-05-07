
from database import Database


class Category:
    table = "category"
    name = None
    
    def __init__(self, name):
        self.name = name

    def save(self):
        db = Database()
        db.save(self)
        