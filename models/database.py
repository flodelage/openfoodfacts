
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
    
        self.mycursor = self.connection.cursor()


