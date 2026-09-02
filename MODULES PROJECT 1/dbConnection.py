
import pymysql

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
