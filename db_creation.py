
import mysql.connector


db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = ""
)

mycursor = db.cursor()

sql = "CREATE DATABASE IF NOT EXISTS openfoodfacts"
mycursor.execute(sql)

sql = "GRANT ALL PRIVILEGES ON openfoodfacts.* TO 'root'@'localhost'"
mycursor.execute(sql)

print("\n La base de données |openfoodfacts| a bien été créée. \n")

db.commit()
