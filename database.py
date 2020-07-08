
import mysql.connector
import requests
from settings import DB_HOST, DB_NAME, DB_PASSWD, DB_USER


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        passwd = DB_PASSWD,
        database = DB_NAME
        )
        self.connection._database = DB_NAME
        self.cursor = self.connection.cursor(buffered=True)

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
        from models.manager import Manager
        for obj in objects_list:
            obj_columns = ""
            obj_values = ""
            for attribute in obj.__dict__.keys():
                if type(obj.__dict__[attribute]) is not list:
                    if isinstance(obj.__dict__[attribute], Manager):
                        pass
                    else:
                        # set object's table:
                        obj_table = obj.table
                        # set object's columns:
                        obj_columns += attribute + "," # add each attribute to the columns string
                        # set object's values:
                        obj_values += f""" "{obj.__dict__[attribute]}" """ + "," # add each value to the values string
            obj_insertion = f"""INSERT IGNORE INTO {obj_table} ({obj_columns[:-1:]}) VALUES ({obj_values[:-1:]})"""
            self.cursor.execute(obj_insertion)
            obj_id = "SET @obj_id = LAST_INSERT_ID()"
            self.cursor.execute(obj_id)

            for attribute in obj.__dict__.keys():
                if type(obj.__dict__[attribute]) is list:
                    for obj in obj.__dict__[attribute]:
                        obj_2nd_columns = ""
                        obj_2nd_values = ""
                        for attribute in obj.__dict__.keys():
                            if isinstance(obj.__dict__[attribute], Manager):
                                pass
                            else:
                                # set object's table:
                                obj_2nd_table = obj.table
                                # set object's columns:
                                obj_2nd_columns += attribute + "," # add each attribute to the columns string
                                # set object's values:
                                obj_2nd_values += f""" "{obj.__dict__[attribute]}" """ + "," # add each value to the values string
                        obj_2nd_insertion = f"""INSERT IGNORE INTO {obj_2nd_table} ({obj_2nd_columns[:-1:]}) VALUES ({obj_2nd_values[:-1:]})"""
                        print(obj_2nd_insertion)
                        self.cursor.execute(obj_2nd_insertion)
                        obj_2nd_id = "SET @obj_2nd_id = LAST_INSERT_ID()"
                        self.cursor.execute(obj_2nd_id)
                        # set many_to_many table
                        m_to_m_table = f"{obj_table}_{obj_2nd_table}"
                        m_to_m_insertion = f"""INSERT IGNORE INTO {m_to_m_table} ({obj_table}_id, {obj_2nd_table}_id) VALUES (@obj_id, @obj_2nd_id)"""
                        self.cursor.execute(m_to_m_insertion)
        self.connection.commit()

    """SELECT QUERIES"""
    def retrieve_id(self, obj):
        table = obj.table # store object's table name
        query = f"SELECT id FROM {table} WHERE name = '{obj.get_name()}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]
        return result

    def retrieve_ids(self, obj):
        table = obj.table # store object's table name
        query = f"SELECT id FROM {table}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def retrieve_all(self, obj):
        table = obj.table # store object's table name
        query = f"SELECT * FROM {table}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def retrieve_columns(self, obj):
        table = obj.table # store object's table name
        query = f"SELECT name, id FROM {table}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def select_all(self, cls):
        self.cursor.execute(f"SELECT name FROM {cls.table}")
        result = self.cursor.fetchall()
        return result
