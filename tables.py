
from settings import DB_NAME


queries = (
f"CREATE TABLE {DB_NAME}.product ("\
"id INT NOT NULL AUTO_INCREMENT,"\
"name VARCHAR(120) NOT NULL,"\
"brand VARCHAR(120),"\
"nutrition_grade VARCHAR(1) NOT NULL,"\
"stores VARCHAR(120),"\
"url VARCHAR(255) NOT NULL,"\
"PRIMARY KEY (id))"\
"ENGINE = INNODB",

f"CREATE TABLE {DB_NAME}.category ("\
"id INT NOT NULL AUTO_INCREMENT,"\
"name VARCHAR(120) NOT NULL,"\
"PRIMARY KEY (id))"\
"ENGINE = INNODB",

f"CREATE TABLE {DB_NAME}.substitute ("\
"id INT NOT NULL AUTO_INCREMENT,"\
"product_id INT NOT NULL,"\
"PRIMARY KEY (id))"\
"ENGINE = INNODB",

f"CREATE TABLE {DB_NAME}.product_category ("\
"category_id INT NOT NULL,"\
"product_id INT NOT NULL,"\
"PRIMARY KEY (category_id, product_id))"\
"ENGINE = INNODB",

f"CREATE TABLE {DB_NAME}.product_substitute ("\
"substitute_id INT NOT NULL,"\
"product_id INT NOT NULL,"\
"PRIMARY KEY (substitute_id, product_id))"\
"ENGINE = INNODB",

# foreign keys :
f"ALTER TABLE {DB_NAME}.substitute "\
"ADD UNIQUE KEY product_id_UNIQUE (product_id),"\
"ADD CONSTRAINT substitute_product_fk FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE",

f"ALTER TABLE {DB_NAME}.product_category "\
"ADD CONSTRAINT prod_cat_category_fk "\
"FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE ON UPDATE CASCADE",

f"ALTER TABLE {DB_NAME}.product_category "\
"ADD CONSTRAINT prod_cat_product_fk "\
f"FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE",

f"ALTER TABLE {DB_NAME}.product_substitute "\
"ADD CONSTRAINT prod_sub_product_fk "\
f"FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE",

f"ALTER TABLE {DB_NAME}.product_substitute "\
"ADD CONSTRAINT prod_sub_substitute_fk "\
f"FOREIGN KEY (substitute_id) REFERENCES substitute(id) ON DELETE CASCADE ON UPDATE CASCADE",
)