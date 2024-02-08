# util/DBConnection.py
from mysql.connector import connect
from assignments.ecommer.util.PropertyUtil import PropertyUtil


def get_connection():
    connection = connect(host='localhost', database='ecom', user='root', password='Kevink25*',
                                         port='3306')
    return connection
