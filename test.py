
from models.entities.product import Product
from models.entities.category import Category
import inspect


prods = Category.objects.all()
for p in prods:
    print(p.name)

