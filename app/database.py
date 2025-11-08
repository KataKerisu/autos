from peewee import *

def connect_db():
    mysql_db = MySQLDatabase(
                        'PysI1234_autos',
                         user='PysI1234_ooo',
                         password='111111',
                         host='10.11.13.118',
                         port=3306)
    return mysql_db

if __name__ == '__main__':
    connect_db().connect()