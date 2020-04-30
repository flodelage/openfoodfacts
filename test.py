import requests

request = requests.get("https://fr.openfoodfacts.org/categorie/pates-a-tartiner-aux-noisettes-et-au-cacao.json")
data = request.json()

a = int(data["count"])
b = data["page_size"]
print(b)


