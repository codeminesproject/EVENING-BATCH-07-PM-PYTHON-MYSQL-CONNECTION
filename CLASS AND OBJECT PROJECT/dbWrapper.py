import pymysql
import config
import logger

class DBConnection:
    def connection(self):
        try:
            dbconnect = pymysql.connect(host=config.hostname,port=config.port,user=config.username,password=config.password,database=config.dbname)

            if dbconnect.open:
                return dbconnect
            else:
                return False
        except Exception as e:
            logger.ErrorLog.log(e,"DBConnection","connection")
            return False

class DBOperation:
    def insert(self,query):
        objDBConnection = DBConnection()
        dbconnect = objDBConnection.connection()
        if type(dbconnect).__name__!="bool":
            cursor = dbconnect.cursor()
            cursor.execute(query)
            dbconnect.commit()
            return True
        else:
            return False

    def update(self,query):
        objDBConnection = DBConnection()
        dbconnect = objDBConnection.connection()
        if type(dbconnect).__name__!="bool":
            cursor = dbconnect.cursor()
            cursor.execute(query)
            dbconnect.commit()
            return True
        else:
            return False

    def delete(self,query):
        objDBConnection = DBConnection()
        dbconnect = objDBConnection.connection()
        if type(dbconnect).__name__!="bool":
            cursor = dbconnect.cursor()
            cursor.execute(query)
            dbconnect.commit()
            return True
        else:
            return False

    def getSingleData(self,query):
        objDBConnection = DBConnection()
        dbconnect = objDBConnection.connection()
        if type(dbconnect).__name__!="bool":
            cursor = dbconnect.cursor()
            cursor.execute(query)
            data = cursor.fetchone()
            return data
        else:
            return False

    def getAllData(self,query):
        objDBConnection = DBConnection()
        dbconnect = objDBConnection.connection()
        if type(dbconnect).__name__!="bool":
            cursor = dbconnect.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        else:
            return False