
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
