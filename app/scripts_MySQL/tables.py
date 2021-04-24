
from app.settings import DB_NAME

tables_queries = (
f"CREATE TABLE {DB_NAME}.product ("\
"id INT NOT NULL AUTO_INCREMENT,"\
"name VARCHAR(120) NOT NULL,"\
"brand VARCHAR(120),"\
"nutrition_grade VARCHAR(1) NOT NULL,"\
"stores VARCHAR(120),"\
"url VARCHAR(255) NOT NULL,"\
"PRIMARY KEY (id),"\
"UNIQUE KEY name_UNIQUE (name))"\
"ENGINE = INNODB",

f"CREATE TABLE {DB_NAME}.category ("\
"id INT NOT NULL AUTO_INCREMENT,"\
"name VARCHAR(120) NOT NULL,"\
"PRIMARY KEY (id),"\
"UNIQUE KEY name_UNIQUE (name))"\
"ENGINE = INNODB",

f"CREATE TABLE {DB_NAME}.substitute ("\
"product INT NOT NULL,"\
"substitute INT NOT NULL,"\
"PRIMARY KEY (product, substitute))"\
"ENGINE = INNODB",

f"CREATE TABLE {DB_NAME}.product_category ("\
"product_id INT NOT NULL,"\
"category_id INT NOT NULL,"\
"PRIMARY KEY (category_id, product_id))"\
"ENGINE = INNODB",

# foreign keys :
f"ALTER TABLE {DB_NAME}.product_category "\
"ADD CONSTRAINT prod_cat_category_fk "\
"FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE ON UPDATE CASCADE",

f"ALTER TABLE {DB_NAME}.product_category "\
"ADD CONSTRAINT prod_cat_product_fk "\
f"FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE",

f"ALTER TABLE {DB_NAME}.substitute "\
"ADD CONSTRAINT sub_substitute_fk "\
f"FOREIGN KEY (substitute) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE",

f"ALTER TABLE {DB_NAME}.substitute "\
"ADD CONSTRAINT sub_product_fk "\
f"FOREIGN KEY (product) REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE",
)
