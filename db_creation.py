
import mysql.connector


db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = ""
)

mycursor = db.cursor()

sql = "DROP DATABASE IF EXISTS openfoodfacts; CREATE DATABASE openfoodfacts CHARACTER SET 'utf8'"
mycursor.execute(sql, multi=True)

sql = "GRANT ALL PRIVILEGES ON openfoodfacts.* TO 'root'@'localhost'"
mycursor.execute(sql)

print("\n La base de données |openfoodfacts| a bien été créée. \n")

db.commit()