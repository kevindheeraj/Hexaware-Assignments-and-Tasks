from mysql import connector
import mysql


class DBUtil:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="Kevink25*",
            database="ticketbookingsystem"
        )

    def getDBConnection(self):
        return self.con.cursor()
