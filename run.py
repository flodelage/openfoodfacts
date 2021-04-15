
import random

import mysql.connector

from database import Database
from requester import Requester
from interface import Interface
from models.entities.category import Category
from models.entities.product import Product
from models.entities.substitute import Substitute
from scripts_MySQL.tables import tables_queries
from settings import DB_NAME


class ProgramManager:
    def __init__(self):
        self.interface = Interface()
        self.db = Database()
        self.req = Requester()

    def run(self):
        run = True
        self.interface.welcome(DB_NAME)

        while run:
            # if openfoodfacts database already exists:
            if self.db.existence_db(DB_NAME) == True:
                """[MAIN MENU]"""
                self.interface.db_management_menu()
                choice = self.interface.prompt_choice()
                if choice == "1":
                    pass
                elif choice == "2":
                    self.db.drop_db(DB_NAME)
                    self.db.create_db(DB_NAME)
                    self.db.create_schema(tables_queries)
                    self.req.get_data()
                elif choice == "3":
                    self.db.drop_db(DB_NAME)
                elif choice == "q":
                    run = False
                    self.interface.goodbye(DB_NAME)
                else:
                    self.interface.choice_error()
            # if openfoodfacts database doen't exists:
            else:
                """[DB CREATION MENU]"""
                self.interface.db_creation_menu()
                choice = self.interface.prompt_choice()
                if choice == "1":
                    self.db.create_db(DB_NAME)
                    self.db.create_schema(tables_queries)
                    self.req.get_data()
                elif choice == "q":
                    run = False
                    self.interface.goodbye(DB_NAME)
                else:
                    self.interface.choice_error()
            self.interface.split()

            """[SUBSTITUTES MENU]"""
            self.interface.find_or_display_substitute_menu()
            choice = self.interface.prompt_choice()
            self.interface.split()

            if choice == "1":
                """[FIND A SUBSTITUTE]"""
                # Display all categories:
                categories = Category.objects.all()
                print("\n Sélectionnez une catégorie: \n")
                self.interface.show_enumerate_list(categories)
                choice = self.interface.prompt_choice()
                category = categories[int(choice) - 1]
                self.interface.split()
                # Display all products in the choosen category:
                print(f"\n / Catégorie: {category.name} / \n")
                products = Product.objects.filter(category__name = category.name)
                print("\n Sélectionnez un produit: \n")
                self.interface.show_enumerate_list(products)
                choice = self.interface.prompt_choice()
                product = products[int(choice) - 1]
                self.interface.split()
                # Display the choosen product:
                print(f"\n / Catégorie: {category.name} > Produit: {product.name} /\n")
                # Substitute
                substitute = ""
                if product.nutrition_grade == "a":
                    print("\n Ce produit a le meilleur nutriscore possible ! \n")
                    substitutes = Product.objects.filter(nutrition_grade = product.nutrition_grade, category__name = category.name)
                    if len(substitutes) == 0:
                        print("\n Nous n'avons pas d'autres produits ayants le nutriscore A dans cette catégorie ! \n")
                    else:
                        for substitute in substitutes:
                            if substitute.name == product.name: substitutes.remove(substitute)
                        print("\n Vous pouvez choisir parmi ces produits ayants également le nutriscore A: \n")
                        self.interface.show_enumerate_list(substitutes)
                        choice = self.interface.prompt_choice()
                        substitute = substitutes[int(choice) - 1]
                        self.interface.split()
                else:
                    substitutes = Product.objects.filter(nutrition_grade__lt = product.nutrition_grade, category__name = category.name)
                    if len(substitutes) == 0:
                        print("\n Nous n'avons trouvé aucun produit ayant un meilleur nutriscore ! \n")
                    else:
                        print(f"\n Vous pouvez choisir parmi ces produits ayants un meilleur nutriscore que {product.nutrition_grade.title()}: \n")
                        substitutes = Product.objects.filter(nutrition_grade__lt = product.nutrition_grade, category__name = category.name)
                        self.interface.show_enumerate_list(substitutes)
                        choice = self.interface.prompt_choice()
                        substitute = substitutes[int(choice) - 1]
                        self.interface.split()
                # . display the substitute
                print(f"\n / Catégorie: {category.name} > Produit: {product.name} > Substitut: {substitute.name} /\n")

                """[SAVE THE SUBSTITUTE]"""
                self.interface.save_substitute_menu()
                choice = self.interface.prompt_choice()
                self.interface.split()
                if choice == "1":
                    sub = Substitute(product=product.id,substitute=substitute.id)
                    try:
                        Substitute.objects.save(sub)
                    except:
                        print(f"""\n Vous avez déjà sauvegardé le substitut "{substitute.name}" pour le produit "{product.name}" ! \n""")
                elif choice == "2":
                    pass
                else:
                    self.interface.choice_error()

            elif choice == "2":
                """[SEE SAVED SUBSTITUTES]"""
                # Display all substitutes:
                substitutes = Substitute.objects.all()
                if substitutes == []:
                    print("\n Vous n'avez pas de substitut sauvegardé ! \n")
                    self.interface.split()
                else:
                    substitutes_models = []
                    for sub in substitutes:
                        substitute = Product.objects.filter(id=sub.substitute)[0]
                        product = Product.objects.filter(id=sub.product)[0]
                        substitutes_models.append({"substitute": substitute, "product": product})
                    print("\n Sélectionnez un substitut: \n")
                    self.interface.show_substitute_enumerate_list(substitutes_models)
                    choice = self.interface.prompt_choice()
                    substitute = substitutes_models[int(choice) - 1]
                    self.interface.split()
                    # Display the choosen substitute product / product substituted:
                    self.interface.show_substitute_and_substituted(substitute)

                    """[MANAGE SAVED SUBSTITUTES]"""
                    self.interface.substitute_management_menu()
                    choice = self.interface.prompt_choice()
                    self.interface.split()
            else:
                self.interface.choice_error()
            if choice == "1":
                pass
            elif choice == "2":
                # Delete the selected substitute
                Substitute.objects.delete(substitute = substitute['substitute'].id,
                                          product= substitute['product'].id)
            else:
                self.interface.choice_error()


    # elif choice == "q":
    #     run = False
    #     self.interface.goodbye(DB_NAME)
    # else:
    #     self.interface.choice_error()
