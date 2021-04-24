
import random

import mysql.connector

from app.utils.database import Database
from app.utils.requester import Requester
from app.views.interface import Interface
from app.models.category import Category
from app.models.product import Product
from app.models.substitute import Substitute
from app.scripts_MySQL.tables import tables_queries
from app.settings import DB_NAME


class ProgramManager:
    """
    Responsability: application process
    """
    def __init__(self):
        self.interface = Interface()
        self.db = Database()
        self.req = Requester()

    def run(self):
        run = True
        self.interface.welcome()
        while run:
            """[MAIN MENU]"""
            self.interface.db_management_menu()
            choice = self.interface.prompt_choice()
            if choice == "1":
                pass
            elif choice == "2":
                self.db.drop_db()
                self.db.create_db()
                self.db.create_schema(tables_queries)
                self.req.get_data()
            elif choice == "q":
                self.interface.goodbye()
                break
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
                self.interface.choose_category()
                self.interface.show_enumerate_list(categories)
                choice = self.interface.prompt_choice()
                category = categories[int(choice) - 1]
                self.interface.split()
                # Display all products in the choosen category:
                self.interface.url_category(category)
                products = Product.objects.filter(category__name = category.name)
                self.interface.choose_product()
                self.interface.show_enumerate_list(products)
                choice = self.interface.prompt_choice()
                product = products[int(choice) - 1]
                self.interface.split()
                # Display the choosen product:
                self.interface.url_product(category, product)
                # Substitute
                substitute = ""
                if product.nutrition_grade == "a":
                    self.interface.best_nutrition_grade()
                    substitutes = Product.objects.filter(nutrition_grade = product.nutrition_grade, category__name = category.name)
                    if len(substitutes) == 0:
                        self.interface.no_other_nutrition_grade_a()
                    else:
                        for substitute in substitutes:
                            if substitute.name == product.name: substitutes.remove(substitute)
                        self.interface.other_nutrition_grade_a()
                        self.interface.show_enumerate_list(substitutes)
                        choice = self.interface.prompt_choice()
                        substitute = substitutes[int(choice) - 1]
                        self.interface.split()
                else:
                    substitutes = Product.objects.filter(nutrition_grade__lt = product.nutrition_grade, category__name = category.name)
                    if len(substitutes) == 0:
                        self.interface.no_better_nutrition_grade()
                    else:
                        self.interface.choose_substitute(product)
                        substitutes = Product.objects.filter(nutrition_grade__lt = product.nutrition_grade, category__name = category.name)
                        self.interface.show_enumerate_list(substitutes)
                        choice = self.interface.prompt_choice()
                        substitute = substitutes[int(choice) - 1]
                        self.interface.split()

                if substitute != "":
                    """[SAVE THE SUBSTITUTE]"""
                    # . display the substitute
                    self.interface.url_substitute(category, product, substitute)
                    self.interface.show_substitute(substitute)
                    self.interface.save_substitute_menu()
                    choice = self.interface.prompt_choice()
                    self.interface.split()
                    if choice == "1":
                        sub = Substitute(product=product.id,substitute=substitute.id)
                        try:
                            Substitute.objects.save(sub)
                            self.interface.save_done(sub)
                            self.interface.split()
                        except:
                            self.interface.save_fail(sub)
                            self.interface.split()
                    elif choice == "2":
                        pass
                    else:
                        self.interface.choice_error()

            elif choice == "2":
                """[SEE SAVED SUBSTITUTES]"""
                # Display all substitutes:
                substitutes = Substitute.objects.all()
                if substitutes == []:
                    self.interface.no_substitute_saved()
                    self.interface.split()
                else:
                    substitutes_models = []
                    for sub in substitutes:
                        substitute = Product.objects.filter(id=sub.substitute)[0]
                        product = Product.objects.filter(id=sub.product)[0]
                        substitutes_models.append({"substitute": substitute, "product": product})
                    self.interface.choose_saved_substitute()
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

                    if choice == "1":
                        # Continue
                        pass
                    elif choice == "2":
                        # Delete the selected substitute
                        try:
                            Substitute.objects.delete(substitute = substitute['substitute'].id,
                                                      product= substitute['product'].id)
                            self.interface.delete_done(substitute)
                        except:
                            self.interface.delete_fail(substitute)
                        self.interface.split()
                    elif choice == "q":
                        self.interface.goodbye()
                        break
                    else:
                        self.interface.choice_error()
            elif choice == "q":
                self.interface.goodbye()
                break
            else:
                self.interface.choice_error()
