
from models.entities.product import Product
from models.entities.category import Category
from models.entities.substitute import Substitute
import inspect
import pprint

pp = pprint.PrettyPrinter(indent=4)

# *** récupérer toutes les catégories *** DONE
# for prod in Product.objects.all():
#     pp.pprint(prod.name)

# *** récupérer tous les produits *** DONE
# for prod in Product.objects.all():
#     pp.pprint(prod)


# *** récupérer tous les produits à partir d'un nom de catégorie *** DONE
# for prod in Product.objects.filter(category__name = 'Produits laitiers'):
#     pp.pprint(prod)

# *** récupérer un produit à partir d'un nom de produit *** DONE
# for prod in Product.objects.filter(name = 'Yaourt brebis miel'):
#     pp.pprint(prod.name)

# *** récupérer les produits ayant un nutriscore inférieur à partir d'un nutriscore et d'une catégorie *** DONE
# for prod in Product.objects.filter(nutrition_grade__lt = 'b', category__name = "yaourts"):
#     pp.pprint(prod.name)

# *** récupérer tous les substituts *** DONE
# for sub in Substitute.objects.all():
#     pp.pprint(sub)

# *** sauvegarder un substitut ***
p = Product.objects.filter(name = 'Yaourt brebis miel')[0]
s = Product.objects.filter(name = "Brassé miel au lait entier")[0]
sub = Substitute(substitute=s.id,product=p.id)
Substitute.objects.save(sub)
