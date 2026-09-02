
from dbConnection import connection

def insert(query):
    dbconnect = connection()
    if type(dbconnect).__name__!="bool":
        cursor = dbconnect.cursor()
        cursor.execute(query)
        dbconnect.commit()
        return True
    else:
        return False

def update(query):
    dbconnect = connection()
    if type(dbconnect).__name__!="bool":
        cursor = dbconnect.cursor()
        cursor.execute(query)
        dbconnect.commit()
        return True
    else:
        return False

def delete(query):
    dbconnect = connection()
    if type(dbconnect).__name__!="bool":
        cursor = dbconnect.cursor()
        cursor.execute(query)
        dbconnect.commit()
        return True
    else:
        return False

def getSingleData(query):
    dbconnect = connection()
    if type(dbconnect).__name__!="bool":
        cursor = dbconnect.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        return data
    else:
        return False

def getAllData(query):
    dbconnect = connection()
    if type(dbconnect).__name__!="bool":
        cursor = dbconnect.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    else:
        return False