
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
    
        self.cursor = self.connection.cursor()

    def create_db(self, db_name):
        existence_query = f"USE {db_name}"
        creation_query = f"CREATE DATABASE {db_name} CHARACTER SET 'utf8' "
        # if openfoodfacts already exists
        try:
            self.cursor.execute(existence_query)
            print(f"\n La base de données |{db_name}| existe déjà \n")
        # if openfoodfacts database doesn't exist
        except:
            try:
        # try to create database
                self.cursor.execute(creation_query)
        # check if openfoodfacts database has been created
                self.cursor.execute(existence_query)   
                print(f"\n La base de données |{db_name}| a bien été créée \n")    
        # if openfoodfacts database has not been created
            except:
                print(f"\n La base de données |{db_name}| n'a pas pu être créée \n")

    def drop_db(self, db_name):
        drop_query = f"DROP DATABASE {db_name}"
        try:
            self.cursor.execute(drop_query)
            print(f"\n La base de données |{db_name}| a bien été supprimée \n")
        except:
            mysql.connector.errors.DatabaseError: "1008 (HY000): Can't drop database 'openfoodfacts'; database doesn't exist"
            print(f"\n La base de données |{db_name}| n'a pas pu être supprimée car elle n'existe pas \n")

    def create_tables(self, db_name):
        self.connection._database = db_name

        query = f"CREATE TABLE {db_name}.product ("\
        "id INT NOT NULL AUTO_INCREMENT,"\
        "name VARCHAR(120) NOT NULL,"\
        "brand VARCHAR(120) NOT NULL,"\
        "nutrition_grade VARCHAR(1) NOT NULL,"\
        "stores VARCHAR(120) NOT NULL,"\
        "url VARCHAR(255) NOT NULL,"\
        "PRIMARY KEY (id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        query = f"CREATE TABLE {db_name}.category ("\
        "id INT NOT NULL AUTO_INCREMENT,"\
        "name VARCHAR(120) NOT NULL,"\
        "PRIMARY KEY (id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        query = f"CREATE TABLE {db_name}.product_category ("\
        "id INT NOT NULL AUTO_INCREMENT,"\
        "category_id INT NOT NULL,"\
        "product_id INT NOT NULL,"\
        "PRIMARY KEY (id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        query = f"CREATE TABLE {db_name}.favorite ("\
        "id INT NOT NULL AUTO_INCREMENT,"\
        "product_id INT NOT NULL,"\
        "PRIMARY KEY (id))"\
        "ENGINE = INNODB"
        self.cursor.execute(query)

        """
        foreign keys
        """
        query = f"ALTER TABLE {db_name}.product_category "\
        "ADD CONSTRAINT prod_cat_category_fk "\
        f"FOREIGN KEY (category_id) REFERENCES {db_name}.category(id) ON DELETE CASCADE ON UPDATE CASCADE"
        self.cursor.execute(query)

        query = f"ALTER TABLE {db_name}.product_category "\
        "ADD CONSTRAINT prod_cat_product_fk "\
        f"FOREIGN KEY (product_id) REFERENCES {db_name}.product(id) ON DELETE CASCADE ON UPDATE CASCADE"
        self.cursor.execute(query)

        query = f"ALTER TABLE {db_name}.favorite "\
        "ADD UNIQUE KEY product_id_UNIQUE (product_id),"\
        "ADD CONSTRAINT favorite_product_fk FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE"
        self.cursor.execute(query)

        self.connection.commit()
        self.connection.close()