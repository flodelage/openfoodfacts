
# OpenFoodFacts
Cette application est le 5e projet du parcours "développeur d'applications - Python" d'Openclassrooms

## Présentation
Il s'agit d'un programme permettant de fournir à l'utilisateur un aliment de substitution plus sain que celui sélectionné.
Pour cela, le programme s'appuie sur les données de l'API d'OpenFoodFacts.

## Description du parcours utilisateur
L'utilisateur lance le programme, et tombe sur le menu principal:
#### Menu Principal
1. Il peut choisir de continuer
2. Il peut choisir de recréer la base de données

#### Menu trouver ou gérer ses substituts
1. Il peut choisir de chercher un substitut à un aliment
2. Il peut choisir de consulter ses substituts sauvegardés

##### choix 1 - Parcours pour trouver un substitut
* Sélectionnez une catégorie. (Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée)
* Sélectionnez un produit. (Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant au produit choisi et appuie sur entrée)
* Sélectionnez un substitut. Le programme propose, si possible, des substituts ayant un meilleur nutriscore que le produit choisi précédemment. (Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant au substitut choisi et appuie sur entrée)
* Le programme affiche alors les détails du susbstitut choisi. Son nom, son nutriscore, sa marque, un magasin où l'acheter et un lien vers la page d'OpenFoodFacts concernant cet aliment.
* L'utilisateur a alors la possibilité d'enregistrer ou non le substitut dans ses favoris.

##### choix 2 - Parcours pour gérer ses substituts
* Sélectionnez un substitut. Le programme affiche, si il y en a, les substituts sauvegardés par l'utilisateur ainsi que le produit qui a été substitué. (Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant au substitut choisi et appuie sur entrée)
* Le programme affiche alors les détails du substitut choisi ainsi que ceux du produit substitué. Leurs noms, nutriscore, marque, magasins et liens vers les pages d'OpenFoodFacts.
* L'utilisateur a alors la possibilité de supprimer ou non le substitut de ses favoris.

### Technologies
* Python 3.8
* OpenFoodFacts' API
* MySQL

## Pour lancer le projet
1. Cloner le repo:
```
git clone https://github.com/flodelage/openfoodfacts.git
```

2. Créer un environnement virtuel:
```
python3 -m venv env
```

3. Activer l'environnement virtuel:
```
source env/bin/activate
```

4. Installer requirements:
```
pip install -r requirements.txt
```

5. Vous pouvez modifier le module settings.py:
* les paramètres de vote base de données:
DB_HOST, DB_USER, DB_PASSWD and DB_NAME
* la constante CATEGORIES en ajoutant les catégories de votre choix, par exemple: CATEGORIES = ["yaourts-au-miel", "jambons-blancs-fumes",]

6. Lancer le projet:
```
python main.py
```
