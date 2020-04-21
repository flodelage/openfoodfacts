
import mysql.connector


class Database:
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd

        self.connection = mysql.connector.connect(
        host = self.host,
        user = self.user,
        passwd = self.passwd
        )
    
        self.mycursor = self.connection.cursor()

    def create(self):
        existence_query = "USE openfoodfacts"
        creation_query = "CREATE DATABASE openfoodfacts CHARACTER SET 'utf8' "
        # if openfoodfacts already exists
        try:
            self.mycursor.execute(existence_query)
            print("\n La base de données |openfoodfacts| existe déjà \n")
        # if openfoodfacts database doesn't exist
        except:
            try:
        # try to create database
                self.mycursor.execute(creation_query)
        # check if openfoodfacts database has been created
                self.mycursor.execute(existence_query)   
                print("\n La base de données |openfoodfacts| a bien été créée \n")    
        # if openfoodfacts database has not been created
            except:
                print("\n La base de données |openfoodfacts| n'a pas pu être créée \n")

    def drop(self):
        drop_query = "DROP DATABASE openfoodfacts"
        try:
            self.mycursor.execute(drop_query)
            print("\n La base de données |openfoodfacts| a bien été supprimée \n")
        except:
            mysql.connector.errors.DatabaseError: "1008 (HY000): Can't drop database 'openfoodfacts'; database doesn't exist"
            print("\n La base de données |openfoodfacts| n'a pas pu être supprimée car elle n'existe pas \n")
