
from models.entities.product import Product
from models.entities.category import Category
from models.entities.substitute import Substitute
import inspect
import pprint

pp = pprint.PrettyPrinter(indent=4)

# *** récupérer toutes les catégories *** DONE
# for prod in Product.objects.filter():
#     pp.pprint(prod.name)

# *** récupérer tous les produits à partir d'un nom de catégorie *** DONE
# for prod in Product.objects.filter(category__name = 'Produits laitiers'):
#     pp.pprint(prod)

# *** récupérer un produit à partir d'un nom de produit *** DONE
# for prod in Product.objects.filter(name = 'Yaourt brebis miel'):
#     pp.pprint(prod.name)

# *** récupérer les produits ayant un nutriscore inférieur à partir d'un nutriscore et d'une catégorie *** DONE
# for prod in Product.objects.filter(nutrition_grade__lt = 'b', category__name = "yaourts"):
#     pp.pprint(prod.name)

# *** sauvegarder un substitut ***
p1 = Product("Naturaplan,Coop,Coop Naturaplan","Jogurt à La Grecque au miel","c","Coop","https://fr.openfoodfacts.org/produit/7611654691709/jogurt-a-la-grecque-au-miel-naturaplan","yaourts,desserts")
sub = Substitute(p1)
subs = [sub]
Substitute.objects.save_all(subs)