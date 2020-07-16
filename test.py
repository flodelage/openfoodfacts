
from models.entities.product import Product
from models.entities.category import Category

cats = Category.objects.all()

for cat in cats:
    print(cat.id,cat.name)
