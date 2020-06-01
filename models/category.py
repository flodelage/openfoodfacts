
class Category():
    table = "category"
    name = None

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def save(self):
        from database import Database
        db = Database()
        db.save(self)