
import mysql.connector
import requests

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
    
        self.cursor = self.connection.cursor()

    def existence_db(self):
        existence_query = "USE openfoodfacts"
        try:
            self.cursor.execute(existence_query)
            return True
        except:
            mysql.connector.errors.ProgrammingError: "1049 (42000): Unknown database 'openfoodfacts'"
            return False

    def create_db(self):
        existence_query = "USE openfoodfacts"
        creation_query = "CREATE DATABASE openfoodfacts CHARACTER SET 'utf8' "
        # if openfoodfacts already exists
        try:
            self.cursor.execute(existence_query)
            print("\n La base de données |openfoodfacts| existe déjà \n")
        # if openfoodfacts database doesn't exist
        except:
            # try to create database
            try:
                self.cursor.execute(creation_query)
        # check if openfoodfacts database has been created
                self.cursor.execute(existence_query)   
                print("\n La base de données |openfoodfacts| a bien été créée \n")    
        # if openfoodfacts database has not been created
            except:
                print("\n La base de données |openfoodfacts| n'a pas pu être créée \n")

    def drop_db(self):
        existence_query = "USE openfoodfacts"
        drop_query = "DROP DATABASE openfoodfacts"
        # try to drop database
        try:
            self.cursor.execute(drop_query)
            # check if openfoodfacts database still exists
            try:
                self.cursor.execute(existence_query)
                # if openfoodfacts database still exists
                print("\n La base de données |openfoodfacts| n'a pas été supprimée \n")
            except:
                # if openfoodfacts database no longer exists
                print("\n La base de données |openfoodfacts| a été supprimée \n")
        # database openfoodfacts can't be droped because it doesn't exists
        except:
            mysql.connector.errors.DatabaseError: "1008 (HY000): Can't drop database 'openfoodfacts'; database doesn't exist"
            print("\n La base de données |openfoodfacts| n'a pas pu être supprimée car elle n'existe pas \n")

    def create_tables(self):
        self.connection._database = "openfoodfacts"

        query = "CREATE TABLE openfoodfacts.product ("\
        "id INT NOT NULL AUTO_INCREMENT,"\
        "name VARCHAR(120) NOT NULL,"\
        "brand VARCHAR(120) NOT NULL,"\
        "nutrition_grade VARCHAR(1) NOT NULL,"\
        "stores VARCHAR(120) NOT NULL,"\
        "url VARCHAR(255) NOT NULL,"\
        "PRIMARY KEY (id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        query = "CREATE TABLE openfoodfacts.category ("\
        "id INT NOT NULL AUTO_INCREMENT,"\
        "name VARCHAR(120) NOT NULL,"\
        "PRIMARY KEY (id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        query = "CREATE TABLE openfoodfacts.product_category ("\
        "id INT NOT NULL AUTO_INCREMENT,"\
        "category_id INT NOT NULL,"\
        "product_id INT NOT NULL,"\
        "PRIMARY KEY (id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        query = "CREATE TABLE openfoodfacts.favorite ("\
        "id INT NOT NULL AUTO_INCREMENT,"\
        "product_id INT NOT NULL,"\
        "PRIMARY KEY (id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        """
        foreign keys
        """
        query = "ALTER TABLE openfoodfacts.product_category "\
        "ADD CONSTRAINT prod_cat_category_fk "\
        "FOREIGN KEY (category_id) REFERENCES openfoodfacts.category(id) ON DELETE CASCADE ON UPDATE CASCADE"
        self.cursor.execute(query)

        query = "ALTER TABLE openfoodfacts.product_category "\
        "ADD CONSTRAINT prod_cat_product_fk "\
        f"FOREIGN KEY (product_id) REFERENCES openfoodfacts.product(id) ON DELETE CASCADE ON UPDATE CASCADE"
        self.cursor.execute(query)

        query = "ALTER TABLE openfoodfacts.favorite "\
        "ADD UNIQUE KEY product_id_UNIQUE (product_id),"\
        "ADD CONSTRAINT favorite_product_fk FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE"
        self.cursor.execute(query)

        self.connection.commit()
        self.connection.close()

    def data_insertion(self):
        self.connection._database = "openfoodfacts"

        request = requests.get("https://fr.openfoodfacts.org/categorie/pates-a-tartiner-aux-noisettes-et-au-cacao.json")
        data = request.json()

        products = data["products"]

        for p in products:
            try:
                query = "INSERT INTO product (name, brand, nutrition_grade, stores, url) VALUES (%s, %s, %s, %s, %s)"
                values = (p['product_name'], p['brands'], p['nutrition_grade_fr'], p['stores'], p['url'])
                self.cursor.execute(query, values)
                self.connection.commit()
            except:
                pass
