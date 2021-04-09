
from models.manager import Manager
from models.entities.substitute import Substitute
from models.entities.product import Product
from models.entities.category import Category


# <<<<<<<<<< test with Category >>>>>>>>>>
c1 = Category("Desserts")
c2 = Category("Yaourts")

def test_category_object_attributes_to_str():
    m = Manager(Category)
    assert m.object_attributes_to_str(c1) == 'name'

def test_category_object_values_to_str():
    m = Manager(Category)
    assert m.object_values_to_str(c1) == ' "Desserts" '

# <<<<<<<<<< test with Product >>>>>>>>>>
p1 = Product("Naturaplan,Coop,Coop Naturaplan","Jogurt à La Grecque au miel","c","Coop","https://fr.openfoodfacts.org/produit/7611654691709/jogurt-a-la-grecque-au-miel-naturaplan","yaourts,desserts")
p2 = Product("Yoplait,Les Laitiers Responsables","Brassé miel au lait entier","b","Carrefour","https://fr.openfoodfacts.org/produit/3329770064522/brasse-miel-au-lait-entier-yoplait","yaourts,desserts")
prods = [p1, p2]

def test_product_object_attributes_to_str():
    m = Manager(Product)
    assert m.object_attributes_to_str(p1) == 'name,brand,nutrition_grade,stores,url'

def test_product_object_values_to_str():
    m = Manager(Product)
    assert m.object_values_to_str(p1) == ' "Jogurt à La Grecque au miel" , "Naturaplan,Coop,Coop Naturaplan" , "c" , "Coop" , "https://fr.openfoodfacts.org/produit/7611654691709/jogurt-a-la-grecque-au-miel-naturaplan" '

# <<<<<<<<<< test with Substitute >>>>>>>>>>
s1 = Substitute(p1)
s2 = Substitute(p2)
subs = [s1, s2]

def test_substitute_object_attributes_to_str():
    m = Manager(Substitute)
    assert m.object_attributes_to_str(s1) == ""

def test_substitute_object_values_to_str():
    m = Manager(Substitute)
    assert m.object_values_to_str(s1) == ""
