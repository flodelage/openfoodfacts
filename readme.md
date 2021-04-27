
# OpenFoodFacts
This application is the 5th project of the Openclassrooms' course "Développeur d'applications - Python"

## Présentation
This is a program to provide the user with a healthier substitute food than the one selected.
For this, the program relies on data from the OpenFoodFacts API.

## Technologies
* Python 3.8
* MySQL
* OpenFoodFacts' API

## Getting started
1. Clone repository:
```
git clone https://github.com/flodelage/openfoodfacts.git
```

2. Create a virtual environment:
```
python3 -m venv env
```

3. Activate the virtual environment:
```
source env/bin/activate
```

4. Install requirements:
```
pip install -r requirements.txt
```

5. You can modify the module app/settings.py:
* your database parameters:
DB_HOST, DB_USER, DB_PASSWD and DB_NAME
* the CATEGORIES constant by adding the categories of your choice, for example: CATEGORIES = ["yaourts-au-miel", "jambons-blancs-fumes",]

6. Run:
```
python main.py
```

## Doc Driven Development (User journey / features)
The user launches the program and arrives on the main menu:
#### Main menu
1. He can choose to continue
2. He can choose to recreate the database

#### Find or manage substitutes menu
1. He can choose to look for a food substitute
2. He can choose to consult his saved substitutes

#### choice 1 - Find a substitute
* Select a category. (Several proposals associated with a number. The user enters the corresponding number and presses Enter)
* Select a product. (Several proposals associated with a number. The user enters the number corresponding to the chosen product and presses Enter)
* Select a substitute. The program offers, if possible, substitutes with a better nutriscore than the product chosen previously. (Several propositions associated with a digit. The user enters the digit corresponding to the chosen substitute and presses Enter)
* The program displays the chosen substitute details. Its name, nutriscore, brand, where to buy it and a link to the OpenFoodFacts page for this food
* The user then can save or not the substitute in his favorites

#### choice 2 - Manage substitutes
* Select a substitute. The program displays, if any, the substitutes saved by the user as well as the product that was substituted. (Several propositions associated with a digit. The user enters the digit corresponding to the chosen substitute and presses Enter)
* The program displays the details of the chosen substitute as well as those of the substituted product. Their names, nutriscore, brand, stores and links to OpenFoodFacts pages
* The user then can removing or not the substitute from his favorites

#### choice 3 - Exit
* Close the program
