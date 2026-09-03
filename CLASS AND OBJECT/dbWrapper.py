import pymysql

class DBConnection:
    def connection():
        try:
            hostname = "localhost"
            port = 3307
            username = "root"
            password = "root"
            dbname = "student_management_system_1"

            dbconnect = pymysql.connect(host=hostname,port=port,user=username,password=password,database=dbname)

            if dbconnect.open:
                return dbconnect
            else:
                return False
        except Exception as e:
            return False

class DBOperation:
    def insert(query):
        dbconnect = DBConnection.connection()
        if type(dbconnect).__name__!="bool":
            cursor = dbconnect.cursor()
            cursor.execute(query)
            dbconnect.commit()
            return True
        else:
            return False

    def update(query):
        dbconnect = DBConnection.connection()
        if type(dbconnect).__name__!="bool":
            cursor = dbconnect.cursor()
            cursor.execute(query)
            dbconnect.commit()
            return True
        else:
            return False

    def delete(query):
        dbconnect = DBConnection.connection()
        if type(dbconnect).__name__!="bool":
            cursor = dbconnect.cursor()
            cursor.execute(query)
            dbconnect.commit()
            return True
        else:
            return False

    def getSingleData(query):
        dbconnect = DBConnection.connection()
        if type(dbconnect).__name__!="bool":
            cursor = dbconnect.cursor()
            cursor.execute(query)
            data = cursor.fetchone()
            return data
        else:
            return False

    def getAllData(query):
        dbconnect = DBConnection.connection()
        if type(dbconnect).__name__!="bool":
            cursor = dbconnect.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        else:
            return False