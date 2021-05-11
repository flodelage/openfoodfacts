
from app.settings import DB_NAME


class View:
    """
    Responsability: manages display in the terminal and user inputs
    """
    # ----- Greetings -----
    def welcome(self):
        """
        Print Hello
        """
        print("\n")
        print("* * * * * * * * * * * * * * * * *")
        print("*                               *")
        print(f"* Bienvenue sur {DB_NAME.capitalize()} ! *")
        print("*                               *")
        print("* * * * * * * * * * * * * * * * *")

    def goodbye(self):
        """
        Print goodbye
        """
        print("\n")
        print("* * * * * * * * * * * * * * * * *")
        print("*                               *")
        print(f"* À bientôt sur {DB_NAME.capitalize()} ! *")
        print("*                               *")
        print("* * * * * * * * * * * * * * * * *")
        print("\n")

    # ----- DB menu -----
    def db_management_menu(self):
        """
        Print db management menu, prompt user and return his choice
        """
        print("\n"
              " 1- Continuer \n"
              " 2- Recréer la base de données")
        return self.prompt_choice()

    # ----- Categories -----
    def find_or_display_substitute_menu(self):
        """
        Print substitute menu, prompt user and return his choice
        """
        print("\n"
              " 1- Trouver un substitut à un aliment \n"
              " 2- Retrouver mes aliments substitués \n"
              " q- Quitter")
        return self.prompt_choice()

    def show_categories(self, categories):
        """
        Print categories list, prompt user and return his choice
        """
        print("\n Sélectionnez une catégorie: \n")
        for num, category in enumerate(categories):
            print(f" {num+1}- {category.name.strip()}")
        return self.prompt_choice()

    def url_category(self, category):
        """
        Print chosen category in url display style
        """
        print(f"\n / Catégorie: {category.name} / \n")

    # ----- Products -----
    def show_products(self, products):
        """
        Print products list, prompt user and return his choice
        """
        print("\n Sélectionnez un produit: \n")
        for num, product in enumerate(products):
            print(f" {num+1}- {product.name.strip()}")
        return self.prompt_choice()

    def url_product(self, category, product):
        """
        Print chosen category and product in url display style
        """
        print(f"\n / Catégorie: {category.name} > Produit: {product.name} /\n")

    def best_nutrition_grade(self):
        print("\n Ce produit a le meilleur nutriscore possible ! \n")

    def no_other_nutrition_grade_a(self):
        print("\n Nous n'avons pas d'autres produits ayants "
              "le nutriscore A dans cette catégorie ! \n")

    def other_nutrition_grade_a(self, products):
        """
        Print better product (nutrition grade == A), prompt user and return his choice
        """
        print("\n Vous pouvez choisir parmi ces produits ayants "
              "également le nutriscore A: \n")
        for num, product in enumerate(products):
            print(f" {num+1}- {product.name.strip()}")
        return self.prompt_choice()

    def no_better_nutrition_grade(self):
        print("\n Nous n'avons trouvé aucun produit "
              "ayant un meilleur nutriscore ! \n")

    def choose_substitute(self, product):
        print("\n Vous pouvez choisir parmi ces produits ayants un"
              f"meilleur nutriscore que {product.nutrition_grade.title()}: \n")

    # ----- Substitutes -----
    def no_substitute_saved(self):
        print("\n Vous n'avez pas de substitut sauvegardé ! \n")

    def url_substitute(self, category, product, better_prod):
        """
        Print chosen category, product and substitute in url display style
        """
        print(f"\n / Catégorie: {category.name} > "
              f"Produit: {product.name} > "
              f"Substitut: {better_prod.name} /\n")

    def save_substitute_menu(self):
        """
        Print save substitute menu, prompt user and return his choice
        """
        print("\n"
              " Voulez-vous sauvegarder ce substitut dans vos favoris ? \n"
              " 1- Oui \n"
              " 2- Non")
        return self.prompt_choice()

    def substitute_management_menu(self):
        """
        Print delete substitute menu, prompt user and return his choice
        """
        print("\n"
              " 1- Continuer \n"
              " 2- Supprimer ce substitut de vos favoris")
        return self.prompt_choice()

    def show_saved_substitutes(self, substitutes):
        """
        Print saved substitutes list, prompt user and return his choice
        """
        for num, sub_prod in enumerate(substitutes):
            print(f" {num+1}- {sub_prod['substitute'].name} "
                  f"(produit substituté: {sub_prod['product'].name})")
        return self.prompt_choice()

    def show_better_products(self, products):
        """
        Print better products list, prompt user and return his choice
        """
        print("\n Sélectionnez un meilleur produit: \n")
        for num, product in enumerate(products):
            print(f" {num+1}- {product.name.strip()}")
        return self.prompt_choice()

    def show_product(self, product):
        print("\n"
              f" {product}\n")

    def show_substitute_and_substituted(self, substitute_dict):
        """
        Print substitute and product substituted details
        """
        print("\n"
              " - Substitut: \n"
              f" {substitute_dict['substitute']}\n"
              "\n"
              " - Produit substitué: \n"
              f" {substitute_dict['product']}\n")

    def save_done(self, substitute):
        print("\n Le substitut a bien été sauvegardé\n")

    def save_fail(self, substitute):
        print("\n Oups ! La sauvegarde du substitut a échoué\n")

    def delete_done(self, substitute):
        """
        Print succeed supression message with details
        """
        print(f"\n Le substitut: {substitute['substitute'].name} "
              f"(produit substituté: {substitute['product'].name}) "
              "a bien été supprimé de vos favoris\n")

    def delete_fail(self, substitute):
        """
        Print failed supression message with details
        """
        print("\n Oups ! La suppresion du substitut: "
              f"{substitute['substitute'].name} "
              f"(produit substituté: {substitute['product'].name}) a échoué\n")

    # ----- User input -----
    def prompt_choice(self):
        """
        Print and prompt user to enter a choice, return the choice
        """
        return input("\n Entrez votre choix >>> ")

    def choice_error(self):
        print("\n Aucun choix ne correspond à la commande saisie ! \n")

    # ----- Split -----
    def split(self):
        """
        Print a line in order to split different menus for more visual clarity
        """
        print("--------------------------------------"
              "--------------------------------------"
              "--------------------------------------"
              "--------------------------------------")
