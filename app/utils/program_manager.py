
import random

import mysql.connector

from app.utils.database import Database
from app.utils.requester import Requester
from app.models.category import Category
from app.models.product import Product
from app.models.substitute import Substitute
from app.scripts_MySQL.tables import tables_queries
from app.settings import DB_NAME
from app.controller.controller import Controller


class ProgramManager:
    """
    Responsability: application process
    """
    def __init__(self):
        self.controller = Controller()
        self.db = Database()
        self.req = Requester()

    def run(self):
        run = True
        self.controller.welcome()
        while run:
            """[MAIN MENU]"""
            self.controller.db_management_menu_process()

            """[SUBSTITUTES MENU]"""
            self.controller.find_or_display_substitute_process()







            # elif choice == "2":
            #     """[SEE SAVED SUBSTITUTES]"""
            #     # Display all substitutes:
            #     substitutes = Substitute.objects.all()
            #     if substitutes == []:
            #         self.interface.no_substitute_saved()
            #         self.interface.split()
            #     else:
            #         substitutes_models = []
            #         for sub in substitutes:
            #             substitute = Product.objects.filter(id=sub.substitute)[0]
            #             product = Product.objects.filter(id=sub.product)[0]
            #             substitutes_models.append({"substitute": substitute, "product": product})
            #         self.interface.choose_saved_substitute()
            #         self.interface.show_substitute_enumerate_list(substitutes_models)
            #         choice = self.interface.prompt_choice()
            #         substitute = substitutes_models[int(choice) - 1]
            #         self.interface.split()
            #         # Display the choosen substitute product / product substituted:
            #         self.interface.show_substitute_and_substituted(substitute)

            #         """[MANAGE SAVED SUBSTITUTES]"""
            #         self.interface.substitute_management_menu()
            #         choice = self.interface.prompt_choice()
            #         self.interface.split()

            #         if choice == "1":
            #             # Continue
            #             pass
            #         elif choice == "2":
            #             # Delete the selected substitute
            #             try:
            #                 Substitute.objects.delete(substitute = substitute['substitute'].id,
            #                                           product= substitute['product'].id)
            #                 self.interface.delete_done(substitute)
            #             except:
            #                 self.interface.delete_fail(substitute)
            #             self.interface.split()
            #         elif choice == "q":
            #             self.interface.goodbye()
            #             break
            #         else:
            #             self.interface.choice_error()
            # elif choice == "q":
            #     self.interface.goodbye()
            #     break
            # else:
            #     self.interface.choice_error()
