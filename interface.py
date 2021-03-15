
class Interface:
    def __init__(self):
        pass

    def welcome(self, db_name):
        print("\n")
        print("* * * * * * * * * * * * * * * * *")
        print("*                               *")
        print(f"* Bienvenue sur {db_name.capitalize()} ! *")
        print("*                               *")
        print("* * * * * * * * * * * * * * * * *")

    def goodbye(self, db_name):
        print(f"\n À bientôt sur {db_name.capitalize()} !")
        print("\n")

    def prompt_choice(self):
        return input("\n Entrez votre choix >>> ")

    def save_substitute_menu(self):
        print("\n"
              " Voulez-vous sauvegarder ce substitut dans vos favoris ? \n"
              " 1- Oui \n"
              " 2- Non")

    def db_management_menu(self):
        print("\n"
              " 1- Continuer \n"
              " 2- Recréer la base de données \n"
              " 3- Supprimer la base de données \n"
              " q- Quitter")

    def db_creation_menu(self):
        print("\n"
              " 1- Créer la base de données \n"
              " q- Quitter")

    def find_or_see_substitute_menu(self):
        print("\n"
              " 1- Trouver un substitut à un aliment \n"
              " 2- Retrouver mes aliments substitués \n"
              " q- Quitter")

    def substitutes_management_menu(self):
        print("\n"
              " 1- Continuer \n"
              " 2- Supprimer ce substitut")

    def __convert_into_enumerate_dict(self, objects_list):
        return {num: obj.name for num, obj in enumerate(objects_list)}

    def show_enumerate_list(self, objects_list):
        enumerate_dict = self.__convert_into_enumerate_dict(objects_list)
        for num, obj_name in enumerate_dict.items():
            print(f" {num+1}- {obj_name.strip()}")

    def choice_error(self):
        print("\n Aucun choix ne correspond à la commande saisie ! \n")

    def split(self):
        print("--------------------------------------------------------------------------------------------------------")
