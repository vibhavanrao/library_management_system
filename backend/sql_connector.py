import mysql.connector

__cnx = None


def sql_connection():
    global __cnx;
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='library_details')
    return __cnx
