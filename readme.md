
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
* Sélectionnez une catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
* Sélectionnez un produit. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant au produit choisi et appuie sur entrée]
* Sélectionnez un substitut. Le programme propose, si possible, des substituts ayant un meilleur nutriscore que le produit choisi précédemment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant au substitut choisi et appuie sur entrée]
* Le programme affiche alors les détails du susbstitut choisi. Son nom, son nutriscore, sa marque, une description, un magasin où l'acheter et un lien vers la page d'OpenFoodFacts concernant cet aliment.
* L'utilisateur a alors la possibilité d'enregistrer ou non le substitut dans ses favoris.

##### choix 2 - Parcours pour gérer ses substituts
* Sélectionnez un substitut. Le programme affiche, si il y en a, les substituts sauvegardés par l'utilisateur ainsi que le produit qui a été substitué. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant au substitut choisi et appuie sur entrée]
* Le programme affiche alors les détails du substitut choisi ainsi que ceux du produit substitué. Leurs noms, nutriscore, marque, description, magasins et liens vers les pages d'OpenFoodFacts.
* L'utilisateur a alors la possibilité de supprimer ou non le substitut de ses favoris.

## Fonctionnalité
* Recherche d'aliments dans la base Open Food Facts.
* L'utilisateur interagit avec le programme dans le terminal ou via une interface graphique.
* Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme doit lui répéter la question.
* La recherche doit s'effectuer sur une base MySql.

## Pré-requis
Il est nécessaire dans un premier temps de créer une base de donnée et de remplir les informations de connexion à cette dernière dans le fichier **password.py.dist** présent dans le répertoire app/model.
Il faut également enlever l'extension dist.

## Installation
Afin de créer les tables et nourrir ces dernières, lors du premier lancement du programme dans le terminal, veuillez rajouter l'argument **-d create**. Voici un exemple si vous êtes placé directement dans le répertoire app/:

```
python3 core.py -d create
```

## Lancement de l'application
Pour lancer l'application, il suffit simplement d'exécuter **core.py**. Si vous êtes dans le répertoire app/:

```
python3 core.py
```

## Options
La mise à jour de la base de données s'effectue automatique si la dernière a eu lieu plus de 7 jours lorsque le programme s'éxecute.
Il est cependant possible de *forcer* la mise à jour avec l'argument **-d update**. Voici un exemple si vous êtes placé directement dans le répertoire app/:

```
python3 core.py -d update
```



