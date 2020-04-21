
from models.database import Database
import mysql.connector


class ProgramManager:
    def __init__(self):
        self.db = Database("localhost", "root", "")


