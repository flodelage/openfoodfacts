
from models.entities.product import Product
from models.entities.category import Category
import inspect
import pprint


# *** récupérer toutes les catégories *** OK
# for cat in Category.objects.all():
#     print(cat)

# *** récupérer tous les produits à partir d'un nom de catégorie *** OK
# for prod in Product.objects.filter(category__name = 'Produits laitiers'):
#     print(prod)

# *** récupérer un produit à partir d'un nom de produit *** OK
# for prod in Product.objects.filter(name = 'Yaourt brebis miel'):
#     print(prod)

# *** récupérer les produits ayant un nutriscore inférieur à partir d'un nutriscore et d'une catégorie *** TO DO
for prod in Product.objects.filter(nutrition_grade__lt = 'c', category__name = 'Produits laitiers'):
    print(prod)