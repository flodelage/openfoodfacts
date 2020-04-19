
import mysql.connector


db = mysql.connector.connect(
  host = "localhost",
  database = 'openfoodfacts',
  user = "root",
  passwd = ""
)

mycursor = db.cursor()

query = "CREATE TABLE openfoodfacts.product ("\
"id INT NOT NULL AUTO_INCREMENT,"\
"name VARCHAR(120) NOT NULL,"\
"brand VARCHAR(120) NOT NULL,"\
"nutrition_grade VARCHAR(1) NOT NULL,"\
"stores VARCHAR(120) NOT NULL,"\
"url VARCHAR(255) NOT NULL,"\
"PRIMARY KEY (id))"\
"ENGINE = INNODB"
mycursor.execute(query)

query = "CREATE TABLE openfoodfacts.category ("\
"id INT NOT NULL AUTO_INCREMENT,"\
"name VARCHAR(120) NOT NULL,"\
"PRIMARY KEY (id))"\
"ENGINE = INNODB"
mycursor.execute(query)

query = "CREATE TABLE openfoodfacts.product_category ("\
"id INT NOT NULL AUTO_INCREMENT,"\
"category_id INT NOT NULL,"\
"product_id INT NOT NULL,"\
"PRIMARY KEY (id))"\
"ENGINE = INNODB"
mycursor.execute(query)

query = "CREATE TABLE openfoodfacts.favorite ("\
"id INT NOT NULL AUTO_INCREMENT,"\
"product_id INT NOT NULL,"\
"PRIMARY KEY (id))"\
"ENGINE = INNODB"
mycursor.execute(query)


"""
foreign keys
"""
query = "ALTER TABLE openfoodfacts.product_category "\
"ADD CONSTRAINT prod_cat_category_fk "\
"FOREIGN KEY (category_id) REFERENCES openfoodfacts.category(id) ON DELETE CASCADE ON UPDATE CASCADE"
mycursor.execute(query)

query = "ALTER TABLE openfoodfacts.product_category "\
"ADD CONSTRAINT prod_cat_product_fk "\
"FOREIGN KEY (product_id) REFERENCES openfoodfacts.product(id) ON DELETE CASCADE ON UPDATE CASCADE"
mycursor.execute(query)

query = "ALTER TABLE openfoodfacts.favorite "\
"ADD UNIQUE KEY product_id_UNIQUE (product_id),"\
"ADD CONSTRAINT favorite_product_fk FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE"
mycursor.execute(query)
