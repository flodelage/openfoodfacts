
import mysql.connector


db = mysql.connector.connect(
  host = "localhost",
  database = 'openfoodfacts',
  user = "root",
  passwd = ""
)

mycursor = db.cursor()