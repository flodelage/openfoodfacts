
class ProductCategory():
    table = "product_category"
    product_id = None
    category_id = None

    def __init__(self, product_id, category_id):
        self.product_id = product_id
        self.category_id = category_id

    def get_product_id(self):
        return self.product_id

    def get_category_id(self):
        return self.category_id

    def save(self):
        from database import Database
        db = Database()
        db.save(self)