
import mysql.connector
from database import Database
from settings import DB_HOST, DB_NAME, DB_PASSWD, DB_USER


class ProgramManager:
    def __init__(self):
        self.db = Database(DB_HOST, DB_USER, DB_PASSWD)

    def run(self):
        run = True
        print(f"\n Bienvenue sur {DB_NAME.capitalize()} !\n")
        while run:
            # if openfoodfacts database already exists
            if self.db.existence_db() == True:
                choice = input(" 1- Continuer \n"
                               " 2- Recréer la base de données \n"
                               " 3- Supprimer la base de données \n"
                               " 4- Quitter \n"
                               "\n Entrez votre choix >>> ")
                if choice == "1":
                    pass
                elif choice == "2":
                    self.db.drop_db()
                    self.db.create_db()
                    self.db.create_tables()
                    self.db.data_insertion()
                elif choice == "3":
                    self.db.drop_db()
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
                    self.db.create_db()
                    self.db.create_tables()
                    self.db.data_insertion()
                elif choice == "2":
                    run = False
                    print("\n À bientôt !\n")
                else:
                    print("\n Aucun choix ne correspond à la commande saisie \n")
