
import requests

r = requests.get('https://fr.openfoodfacts.org/categorie/produits-a-tartiner/1.json')
data = r.json()
p1 = data['products'][0]

print(p1["ingredients_text_fr"])