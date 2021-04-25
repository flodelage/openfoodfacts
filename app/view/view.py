
from app.settings import DB_NAME

class View:
    """
    Responsability: manage the display for the user
    """
    # ----- Greetings -----
    def welcome(self):
        print("\n")
        print("* * * * * * * * * * * * * * * * *")
        print("*                               *")
        print(f"* Bienvenue sur {DB_NAME.capitalize()} ! *")
        print("*                               *")
        print("* * * * * * * * * * * * * * * * *")

    def goodbye(self):
        print("\n")
        print("* * * * * * * * * * * * * * * * *")
        print("*                               *")
        print(f"* À bientôt sur {DB_NAME.capitalize()} ! *")
        print("*                               *")
        print("* * * * * * * * * * * * * * * * *")
        print("\n")

    # ----- DB menu -----
    def db_management_menu(self):
        print("\n"
              " 1- Continuer \n"
              " 2- Recréer la base de données \n"
              " q- Quitter")
        return self.prompt_choice()

    # ----- Categories -----
    def find_or_display_substitute_menu(self):
        print("\n"
              " 1- Trouver un substitut à un aliment \n"
              " 2- Retrouver mes aliments substitués \n"
              " q- Quitter")
        return self.prompt_choice()

    def show_categories(self, categories):
        print("\n Sélectionnez une catégorie: \n")
        for num, category in enumerate(categories):
            print(f" {num+1}- {category.name.strip()}")
        return self.prompt_choice()

    def url_category(self, category):
        print(f"\n / Catégorie: {category.name} / \n")

    # ----- Products -----
    def show_products(self, products):
        print("\n Sélectionnez un produit: \n")
        for num, product in enumerate(products):
            print(f" {num+1}- {product.name.strip()}")
        return self.prompt_choice()

    def url_product(self, category, product):
        print(f"\n / Catégorie: {category.name} > Produit: {product.name} /\n")

    def best_nutrition_grade(self):
        print("\n Ce produit a le meilleur nutriscore possible ! \n")

    def no_other_nutrition_grade_a(self):
        print("\n Nous n'avons pas d'autres produits ayants le nutriscore A dans cette catégorie ! \n")

    def other_nutrition_grade_a(self, products):
        print("\n Vous pouvez choisir parmi ces produits ayants également le nutriscore A: \n")
        for num, product in enumerate(products):
            print(f" {num+1}- {product.name.strip()}")
        return self.prompt_choice()

    def no_better_nutrition_grade(self):
        print("\n Nous n'avons trouvé aucun produit ayant un meilleur nutriscore ! \n")

    def choose_substitute(self, product):
        print(f"\n Vous pouvez choisir parmi ces produits ayants un meilleur nutriscore que {product.nutrition_grade.title()}: \n")

    # ----- Substitutes -----
    def no_substitute_saved(self):
        print("\n Vous n'avez pas de substitut sauvegardé ! \n")

    def url_substitute(self, category, product, better_prod):
        print(f"\n / Catégorie: {category.name} > Produit: {product.name} > Substitut: {better_prod.name} /\n")

    def save_substitute_menu(self):
        print("\n"
              " Voulez-vous sauvegarder ce substitut dans vos favoris ? \n"
              " 1- Oui \n"
              " 2- Non")
        return self.prompt_choice()

    def substitute_management_menu(self):
        print("\n"
              " 1- Continuer \n"
              " 2- Supprimer ce substitut de vos favoris")
        return self.prompt_choice()

    def show_saved_substitutes(self, substitutes):
        for num, sub_prod in enumerate(substitutes):
            print(f" {num+1}- {sub_prod['substitute'].name} (produit substituté: {sub_prod['product'].name})")
        return self.prompt_choice()

    def show_better_products(self, products):
        print("\n Sélectionnez un meilleur produit: \n")
        for num, product in enumerate(products):
            print(f" {num+1}- {product.name.strip()}")
        return self.prompt_choice()

    def show_product(self, product):
        print("\n"
             f" {product}\n")

    def show_substitute_and_substituted(self, substitute_dict):
        print("\n"
              " - Substitut: \n"
             f" {substitute_dict['substitute']}\n"
              "\n"
              " - Produit substitué: \n"
             f" {substitute_dict['product']}\n")

    def save_done(self, substitute):
        print(f"\n Le substitut a bien été sauvegardé\n")

    def save_fail(self, substitute):
        print(f"\n Oups ! La sauvegarde du substitut a échoué\n")

    def delete_done(self, substitute):
        print(f"\n Le substitut: {substitute['substitute'].name} (produit substituté: {substitute['product'].name}) a bien été supprimé de vos favoris\n")

    def delete_fail(self, substitute):
        print(f"\n Oups ! La suppresion du substitut: {substitute['substitute'].name} (produit substituté: {substitute['product'].name}) a échoué\n")

    # ----- User input -----
    def prompt_choice(self):
        return input("\n Entrez votre choix >>> ")

    def choice_error(self):
        print("\n Aucun choix ne correspond à la commande saisie ! \n")

    # ----- Split -----
    def split(self):
        print("-----------------------------------------------------------------------------"
              "-----------------------------------------------------------------------------")
