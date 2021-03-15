
from models.entities.product import Product
from models.entities.category import Category
import inspect
import pprint

pp = pprint.PrettyPrinter(indent=4)

# *** récupérer toutes les catégories *** DONE
# for prod in Product.objects.all():
#     print(prod)

# *** récupérer tous les produits à partir d'un nom de catégorie *** DONE
# for prod in Product.objects.filter(category__name = 'Produits laitiers'):
#     pp.pprint(prod)

# *** récupérer un produit à partir d'un nom de produit *** DONE
# for prod in Product.objects.filter(name = 'Yaourt brebis miel'):
#     pp.pprint(prod.name)

# *** récupérer les produits ayant un nutriscore inférieur à partir d'un nutriscore et d'une catégorie *** DONE
for prod in Product.objects.filter(nutrition_grade__lt = 'b', category__name = "yaourts"):
    pp.pprint(prod.name)