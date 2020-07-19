
from models.entities.product import Product
from models.entities.category import Category
import inspect




# cats = Category.objects.all()

# for c in cats:
#     print(c.id,c.name)


a = {'brand': None, 'category': [], 'name': None, 'nutrition_grade': None, 'stores': None, 'url': None}

for value in a.values():
    if isinstance(value, list) == True:
        print(value)

