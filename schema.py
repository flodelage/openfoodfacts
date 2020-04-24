
import mysql.connector
from models.database import Database

class Schema:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = Database("localhost", "root", "")

