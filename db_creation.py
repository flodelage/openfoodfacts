
import mysql.connector


db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = ""
)

mycursor = db.cursor()

q_existence = "USE openfoodfacts"
q_creation = "CREATE DATABASE openfoodfacts CHARACTER SET 'utf8' "

query = "DROP DATABASE openfoodfacts"
mycursor.execute(query)

# check if openfoodfacts database already exists
try:
    mycursor.execute(q_existence)
    print("\n La base de données |openfoodfacts| existe déjà \n")
# if openfoodfacts database already exists
except:
    try:
# try to create database
        mycursor.execute(q_creation)
# check if openfoodfacts database has been created
        mycursor.execute(q_existence)   
        print("\n La base de données |openfoodfacts| a bien été créée. \n")    
# if openfoodfacts database has not been created
    except:
        print("\n La base de données |openfoodfacts| n'a pas pu être créée. \n")

db.commit()
db.close()
