



class Category():
    table = "category"
    name = None

    def __init__(self, name):
        self.name = name

    def save(self, db):
        db.save(self)

    def get_name(self):
        return self.name