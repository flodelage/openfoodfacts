
from models.entities.product import Product
from models.entities.category import Category
import inspect
import pprint

pp = pprint.PrettyPrinter(indent=4)
prods = Product.objects.filter(nutrition_grade='c', stores='monoprix', category__name='Produits laitiers')
for prod in prods:
    pp.pprint(prod)

# cats = Category.objects.filter(name='Produits laitiers', product__nutrition_grade='c')
# print(prods)
