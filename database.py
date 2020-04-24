
import mysql.connector
import requests
from settings import DB_HOST, DB_NAME, DB_PASSWD, DB_USER

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
        existence_query = f"USE {DB_NAME}"
        try:
            self.cursor.execute(existence_query)
            return True
        except:
            mysql.connector.errors.ProgrammingError: f"1049 (42000): Unknown database '{DB_NAME}'"
            return False

    def create_db(self):
        existence_query = f"USE {DB_NAME}"
        creation_query = f"CREATE DATABASE {DB_NAME} CHARACTER SET 'utf8' "
        # if openfoodfacts already exists
        try:
            self.cursor.execute(existence_query)
            print(f"\n La base de données |{DB_NAME}| existe déjà \n")
        # if openfoodfacts database doesn't exist
        except:
            # try to create database
            try:
                self.cursor.execute(creation_query)
        # check if openfoodfacts database has been created
                self.cursor.execute(existence_query)   
                print(f"\n La base de données |{DB_NAME}| a bien été créée \n")    
        # if openfoodfacts database has not been created
            except:
                print(f"\n La base de données |{DB_NAME}| n'a pas pu être créée \n")

    def drop_db(self):
        existence_query = f"USE {DB_NAME}"
        drop_query = f"DROP DATABASE {DB_NAME}"
        # try to drop database
        try:
            self.cursor.execute(drop_query)
            # check if openfoodfacts database still exists
            try:
                self.cursor.execute(existence_query)
                # if openfoodfacts database still exists
                print(f"\n La base de données |{DB_NAME}| n'a pas été supprimée \n")
            except:
                # if openfoodfacts database no longer exists
                print(f"\n La base de données |{DB_NAME}| a été supprimée \n")
        # database openfoodfacts can't be droped because it doesn't exists
        except:
            mysql.connector.errors.DatabaseError: f"1008 (HY000): Can't drop database '{DB_NAME}'; database doesn't exist"
            print(f"\n La base de données |{DB_NAME}| n'a pas pu être supprimée car elle n'existe pas \n")

    def create_tables(self):
        self.connection._database = f"{DB_NAME}"

        query = f"CREATE TABLE {DB_NAME}.product ("\
        "id INT NOT NULL AUTO_INCREMENT,"\
        "name VARCHAR(120) NOT NULL,"\
        "brand VARCHAR(120),"\
        "nutrition_grade VARCHAR(1) NOT NULL,"\
        "stores VARCHAR(120),"\
        "url VARCHAR(255) NOT NULL,"\
        "PRIMARY KEY (id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        query = f"CREATE TABLE {DB_NAME}.category ("\
        "id INT NOT NULL AUTO_INCREMENT,"\
        "name VARCHAR(120) NOT NULL,"\
        "PRIMARY KEY (id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        query = f"CREATE TABLE {DB_NAME}.substitute ("\
        "id INT NOT NULL AUTO_INCREMENT,"\
        "product_id INT NOT NULL,"\
        "PRIMARY KEY (id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        query = f"CREATE TABLE {DB_NAME}.product_category ("\
        "category_id INT NOT NULL,"\
        "product_id INT NOT NULL,"\
        "PRIMARY KEY (category_id, product_id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        query = f"CREATE TABLE {DB_NAME}.product_substitute ("\
        "substitute_id INT NOT NULL,"\
        "product_id INT NOT NULL,"\
        "PRIMARY KEY (substitute_id, product_id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        """
        foreign keys
        """
        query = f"ALTER TABLE {DB_NAME}.substitute "\
        "ADD UNIQUE KEY product_id_UNIQUE (product_id),"\
        "ADD CONSTRAINT substitute_product_fk FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE"
        self.cursor.execute(query)

        query = f"ALTER TABLE {DB_NAME}.product_category "\
        "ADD CONSTRAINT prod_cat_category_fk "\
        "FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE ON UPDATE CASCADE"
        self.cursor.execute(query)

        query = f"ALTER TABLE {DB_NAME}.product_category "\
        "ADD CONSTRAINT prod_cat_product_fk "\
        f"FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE"
        self.cursor.execute(query)

        query = f"ALTER TABLE {DB_NAME}.product_substitute "\
        "ADD CONSTRAINT prod_sub_product_fk "\
        f"FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE"
        self.cursor.execute(query)

        query = f"ALTER TABLE {DB_NAME}.product_substitute "\
        "ADD CONSTRAINT prod_sub_substitute_fk "\
        f"FOREIGN KEY (substitute_id) REFERENCES substitute(id) ON DELETE CASCADE ON UPDATE CASCADE"
        self.cursor.execute(query)
        self.connection.commit()

    def data_insertion(self):
        self.connection._database = f"{DB_NAME}"

        pages = range(1, 7)

        for page in pages:
            request = requests.get(f"https://fr.openfoodfacts.org/categorie/pates-a-tartiner-aux-noisettes-et-au-cacao/{page}.json")
            data = request.json()
            products = data["products"]

            for p in products:
                try:
                    query = "INSERT INTO product (name, brand, nutrition_grade, stores, url) VALUES (%s, %s, %s, %s, %s)"
                    values = (p['product_name'], p['brands'], p['nutrition_grades'], p['stores'], p['url'])
                    self.cursor.execute(query, values)
                    self.connection.commit()
                except KeyError:
                    continue


                    # query = f"INSERT INTO category (name) VALUES ({p['categories']})"
                    # self.cursor.execute(query)
                    # self.connection.commit()
