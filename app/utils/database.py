
import mysql.connector
from app.settings import DB_HOST, DB_NAME, DB_PASSWD, DB_USER


class Database:
    """
    Responsabilities:
    Connection to the database.
    Creation, deletion, settlement of the database
    """
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWD,
            database=DB_NAME
        )
        self.cursor = self.connection.cursor(buffered=True)

    def create_db(self):
        """
        create database and use it
        """
        creation_query = f"CREATE DATABASE {DB_NAME} CHARACTER SET 'utf8mb4' "
        existence_query = f"USE {DB_NAME}"
        try:
            self.cursor.execute(creation_query)
            self.cursor.execute(existence_query)
            print(f"\n La base de données |{DB_NAME}| a été créée \n")
        except:
            print("\n Une erreur s'est produite lors "
                  "de la création de la base de données \n")

    def drop_db(self):
        """
        drop database
        """
        drop_query = f"DROP DATABASE {DB_NAME}"
        try:
            self.cursor.execute(drop_query)
            print(f"\n La base de données |{DB_NAME}| a été supprimée \n")
        except:
            print("\n Une erreur s'est produite lors "
                  "de la suppression de la base de données \n")

    def create_tables(self, script):
        """
        create the tables by calling an SQL script
        """
        for query in script:
            try:
                self.cursor.execute(query)
            except:
                print("\n Une erreur s'est produite lors "
                      "de la création des tables \n")
        print("\n Les tables ont bien été créées "
              f"dans la base de données |{DB_NAME}|  \n")
