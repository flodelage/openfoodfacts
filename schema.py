
import mysql.connector
from database import Database
from settings import DB_HOST, DB_USER, DB_PASSWD, DB_NAME


class Schema:
    def __init__(self, db):
        self.db = Database(DB_HOST, DB_USER, DB_PASSWD)
        self.db.existing_db_connection(DB_NAME)

    def create_tables(self, script):
        for query in script:
            self.db.cursor.execute(query)
