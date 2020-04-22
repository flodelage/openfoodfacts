
from models.database import Database
import mysql.connector


class ProgramManager:
    def __init__(self):
        self.db = Database("localhost", "root", "")

    def run(self):
        run = True
        print("\n Bienvenue sur OpenFoodFacts !\n")
        while run:
            choice = input(" 1- Déjà utilisateur ? \n"
                           " 2- Nouvel utilisateur ? \n"
                           " 3- Quitter \n"
                           "\n Entrez votre choix >>> ")
            if choice == "1":
                db_name = input("\n Entrez le nom de votre base de données >>> ")
                db_name = db_name.lower()
                q = f"USE {db_name}"
                try:
                    self.db.cursor.execute(q)
                    print(f"\n Bienvenue sur votre base de données |{db_name}| \n")
                except:
                    print(f"\n La base de données |{db_name}| n'existe pas \n")

            elif choice == "2":
                db_name = input("\n Entrer le nom de la base de données que vous souhaitez créer >>> ")
                db_name = db_name.lower()
                self.db.create_db(db_name)
                q = f"USE {db_name}"
                print(f"\n Bienvenue sur votre base de données |{db_name}| \n")

            elif choice == "3":
                run = False
                print(f"\n À bientôt !\n")
            else:
                print("\n Aucun choix ne correspond à la commande saisie \n")
