
from models.entities.product import Product
from models.entities.category import Category
import inspect


prods = Product.objects.filter(nutriscore='c', category__name='Produits laitiers')
