
import mysql.connector
import requests
from settings import DB_HOST, DB_NAME, DB_PASSWD, DB_USER
from models.product import Product
from models.category import Category


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        passwd = DB_PASSWD,
        database= DB_NAME
        )
        self.connection._database = DB_NAME
        self.cursor = self.connection.cursor()

    def existence_db(self, db_name):
        existence_query = f"USE {db_name}"
        try:
            self.cursor.execute(existence_query)
            return True
        except:
            return False

    def create_db(self, db_name):
        existence_query = f"USE {db_name}"
        creation_query = f"CREATE DATABASE {db_name} CHARACTER SET 'utf8mb4' "
        # if openfoodfacts already exists
        try:
            self.cursor.execute(existence_query)
            print(f"\n La base de données |{db_name}| existe déjà \n")
        # if openfoodfacts database doesn't exist
        except:
            # try to create database
            try:
                self.cursor.execute(creation_query)
        # check if openfoodfacts database has been created
                self.cursor.execute(existence_query)
                print(f"\n La base de données |{db_name}| a bien été créée \n")
        # if openfoodfacts database has not been created
            except:
                print(f"\n La base de données |{db_name}| n'a pas pu être créée \n")

    def drop_db(self, db_name):
        existence_query = f"USE {db_name}"
        drop_query = f"DROP DATABASE {db_name}"
        # try to drop database
        try:
            self.cursor.execute(drop_query)
            # check if openfoodfacts database still exists
            try:
                self.cursor.execute(existence_query)
                # if openfoodfacts database still exists
                print(f"\n La base de données |{db_name}| n'a pas été supprimée \n")
            except:
                # if openfoodfacts database no longer exists
                print(f"\n La base de données |{db_name}| a été supprimée \n")
        # database openfoodfacts can't be droped because it doesn't exists
        except mysql.connector.errors.DatabaseError:
            print(f"\n La base de données |{db_name}| n'a pas pu être supprimée car elle n'existe pas \n")

    def create_schema(self, script):
        self.connection._database = DB_NAME
        for query in script:
            self.cursor.execute(query)

    def save(self, obj):
        table = obj.table # store Product's table name
        params = obj.__dict__.keys() # store object's parameters
        args = obj.__dict__.values() # store object's arguments
        columns = ", ".join(params) # set string of params
        values_qty = f"%s, " * len(params) # set number of "%s ," equal to the number of the object's params
        values_qty = values_qty.strip()[:-1:] # remove ending space then ending ","
        if len(params) == 1:
            query = f"INSERT INTO {table} ({columns}) VALUES ('{tuple(args)[0]}')"
            self.cursor.execute(query)
        else:
            query = f"INSERT INTO {table} ({columns}) VALUES ({values_qty})"
            values = tuple(args)
            self.cursor.execute(query, values)
        self.connection.commit()

    def save_all(self, objects_list):
        values_all = ""
        for obj in objects_list:
            table = obj.table # store Product's table name
            params = obj.__dict__.keys() # store object's parameters
            args = obj.__dict__.values() # store object's arguments
            columns = ", ".join(params) # set string of params
            values = ""
            for val in args:
                value = f"'{val.strip()}',"
                values += value
            values = f"({values[:-1:]}),"
            values_all += values
        values_all = values_all[:-1:]

        query = f"INSERT INTO {table} ({columns}) VALUES {values_all}"
        print(query)
        self.cursor.execute(query)
        self.connection.commit()

    def select_all(self, table):
        self.cursor.execute(f"SELECT name FROM {table}")
        result = self.cursor.fetchall()
        return result
