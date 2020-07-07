
import random
from database import Database

import mysql.connector
from requester import Requester
from interface import Interface
from models.entities.category import Category
from scripts_MySQL.tables import tables_queries
from settings import DB_NAME, NUTRITION_GRADES


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
            self.interface.find_or_see_substitute_menu()
            choice = self.interface.prompt_choice()
            self.interface.split()
            if choice == "1":
                """[FIND A SUBSTITUTE]"""
                # Display all categories:
                categories = self.db.select_all(Category)
                categories_dict = {}
                for num, cat_name in enumerate(categories):
                    categories_dict[num+1] = cat_name[0]
                print("\n Sélectionnez une catégorie: \n")
                self.interface.show_enumerate_list(categories_dict)
                choice = self.interface.prompt_choice()
                self.interface.split()
                # Display all products in the choosen category:
                query = f"SELECT product.name FROM product INNER JOIN product_category On product_category.product_id = product.id INNER JOIN category ON product_category.category_id = category.id WHERE category.name = '{categories_dict[int(choice)]}'"
                self.db.cursor.execute(query)
                products = self.db.cursor.fetchall()
                products_dict = {}
                for num, prod_name in enumerate(products):
                    products_dict[num+1] = prod_name[0]
                print("\n Sélectionnez un produit: \n")
                self.interface.show_enumerate_list(products_dict)
                choice = self.interface.prompt_choice()
                self.interface.split()
                # Display the choosen product:
                print(products_dict[int(choice)])
                query = f"SELECT name FROM product WHERE product.name = '{products_dict[int(choice)]}'"
                self.db.cursor.execute(query)
                product_name = self.db.cursor.fetchone()[0]
                # Display the substitute:
                # . retrieve product nutrition_grade
                query = f"SELECT nutrition_grade FROM product WHERE product.name = '{products_dict[int(choice)]}'"
                self.db.cursor.execute(query)
                product_nutr_grade = self.db.cursor.fetchone()[0]
                # . retrieve product categories
                query = f"SELECT category_id FROM openfoodfacts.product_category INNER JOIN product ON product_id = product.id WHERE product.name = '{products_dict[int(choice)]}'"
                self.db.cursor.execute(query)
                product_categories = self.db.cursor.fetchall()
                # . set better nutrition grades
                better_nutr_grades = NUTRITION_GRADES[:NUTRITION_GRADES.index(product_nutr_grade)]
                # .
                if product_nutr_grade == "a":
                    print("Ce produit a le meilleur nutriscore possible !")
                else:
                    nutr_string = ""
                    all_better_products = []
                    for nutr in better_nutr_grades:
                        nutr_string += f"product.nutrition_grade = '{nutr}' OR "
                    nutr_string = nutr_string[:-4]
                    for cat in product_categories:
                        query = f"""SELECT product.name FROM product INNER JOIN product_category ON product_id = product.id WHERE product_category.category_id = {cat[0]} AND ({nutr_string})"""
                        self.db.cursor.execute(query)
                        for prod in self.db.cursor.fetchall():
                            all_better_products.append(prod)
                    if all_better_products:
                        print("Voici le substitut que nous vous proposons:")
                        substitute_name = random.choice(all_better_products)[0]
                        # . display the substitute
                        print(substitute_name)
                        # Save the substitute:
                        self.interface.save_substitute_menu()
                        choice = self.interface.prompt_choice()
                        self.interface.split()
                        if choice == "1":
                            # . retrieve product id
                            query = f"""SELECT product.id FROM product INNER JOIN product_category ON product_id = product.id WHERE product.name = '{product_name}'"""
                            self.db.cursor.execute(query)
                            product_id = self.db.cursor.fetchone()[0]
                            # . retrieve substitute id
                            query = f"""SELECT product.id FROM product INNER JOIN product_category ON product_id = product.id WHERE product.name = '{substitute_name}'"""
                            self.db.cursor.execute(query)
                            substitute_id = self.db.cursor.fetchone()[0]
                            # . save the substitute
                            query = f"""INSERT INTO substitute (product_id, substitute_id) VALUES ('{product_id}', '{substitute_id}')"""
                            try:
                                self.db.cursor.execute(query)
                                self.db.connection.commit()
                            except:
                                print(f"Vous avez déjà sauvegardé ce substitut pour le produit {product_name}")
                        elif choice == "2":
                            pass
                        else:
                            self.interface.choice_error()
                    else:
                        print("Nous n'avons trouvé aucun produit ayant un meilleur nutriscore !")
            elif choice == "2":
                """[SEE SAVED SUBSTITUTES]"""
                query = "SELECT product.name FROM product INNER JOIN substitute ON substitute.substitute_id = product.id"
                self.db.cursor.execute(query)
                substitutes = self.db.cursor.fetchall()
                if not substitutes:
                    print("Vous n'avez pas de substitut sauvegardé !")
                else:
                    # Display of all saved substitutes:
                    print("\n Voici vos substituts sauvegardés: \n")
                    substitutes_dict = {}
                    for num, subst_name in enumerate(substitutes):
                        substitutes_dict[num+1] = subst_name[0]
                    self.interface.show_enumerate_list(substitutes_dict)
                    choice = self.interface.prompt_choice()
                    self.interface.split()
                    if int(choice) in substitutes_dict.keys():
                        # Display a substitute and the substituted product:
                        # - the substitute:
                        query = f"SELECT * FROM product WHERE product.name = '{substitutes_dict[int(choice)]}'"
                        self.db.cursor.execute(query)
                        substitute = self.db.cursor.fetchone()
                        print(f"le substitut: {substitute}")
                        # - the substituted product:
                        # . retrieve substitute id
                        query = f"SELECT id FROM product WHERE product.name = '{substitutes_dict[int(choice)]}'"
                        self.db.cursor.execute(query)
                        substitute_id = self.db.cursor.fetchone()[0]
                        # . retrieve substituted product id
                        query = f"SELECT product_id FROM substitute WHERE substitute_id = {substitute_id}"
                        self.db.cursor.execute(query)
                        product_id = self.db.cursor.fetchone()[0]
                        # . retrieve substituted product
                        query = f"SELECT * FROM product WHERE product.id = {product_id}"
                        self.db.cursor.execute(query)
                        product = self.db.cursor.fetchone()
                        print(f"le produit substitué: {product}")
                        """[MANAGE SAVED SUBSTITUTES]"""
                        self.interface.substitutes_management_menu()
                        choice = self.interface.prompt_choice()
                        self.interface.split()
                    else:
                        self.interface.choice_error()
                    if choice == "1":
                        # continue
                        pass
                    elif choice == "2":
                        # Delete the selected substitute
                        query = f"DELETE FROM substitute WHERE substitute_id = {substitute_id} AND product_id = {product_id}"
                        self.db.cursor.execute(query)
                        self.db.connection.commit()
                    else:
                        self.interface.choice_error()
            elif choice == "q":
                run = False
                self.interface.goodbye(DB_NAME)
            else:
                self.interface.choice_error()
