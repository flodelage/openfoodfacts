
from database import Database
from requester import Requester
from models.category import Category
from scripts_MySQL.tables import tables_queries
from settings import DB_NAME


class ProgramManager:
    def __init__(self):
        self.db = Database()
        self.req = Requester()

    def run(self):
        run = True
        print(f"\n Bienvenue sur {DB_NAME.capitalize()} ! \n")
        while run:

            """[DB CREATION]"""
            # if openfoodfacts database already exists
            if self.db.existence_db(DB_NAME) == True:
                choice = input(" 1- Continuer \n"
                               " 2- Recréer la base de données \n"
                               " 3- Supprimer la base de données \n"
                               " 4- Quitter \n"
                               "\n Entrez votre choix >>> ")
                if choice == "1":
                    pass
                elif choice == "2":
                    self.db.drop_db(DB_NAME)
                    self.db.create_db(DB_NAME)
                    self.db.create_schema(tables_queries)
                    self.req.insert_data()
                elif choice == "3":
                    self.db.drop_db(DB_NAME)
                elif choice == "4":
                    run = False
                    print("\n À bientôt !\n")
                else:
                    print("\n Aucun choix ne correspond à la commande saisie \n")

            # if openfoodfacts database doen't exists
            else:
                choice = input(" 1- Créer la base de données \n"
                               " 2- Quitter \n"
                               "\n Entrez votre choix >>> ")
                if choice == "1":
                    self.db.create_db(DB_NAME)
                    self.db.create_schema(tables_queries)
                    self.req.insert_data()
                elif choice == "2":
                    run = False
                    print("\n À bientôt !\n")
                else:
                    print("\n Aucun choix ne correspond à la commande saisie \n")


            """[MAIN MENU]"""
            choice = input(" 1- Trouver un substitut à un aliment \n"
                           " 2- Retrouver mes aliments substitués \n"
                           " 3- Quitter \n"
                           "\n Entrez votre choix >>> ")

            if choice == "1":
                categories = self.db.select_all(Category.table)
                for num, cat in enumerate(categories):
                    print(f" {num+1}- {cat[0].strip()}")
                choice = input("\n Entrez votre choix >>> ")

            elif choice == "2":
                # afficher la liste des favoris
                pass
            elif choice == "3":
                run = False
                print("\n À bientôt !\n")
            else:
                print("\n Aucun choix ne correspond à la commande saisie \n")