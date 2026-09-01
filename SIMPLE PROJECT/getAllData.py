import pymysql

hostname = "localhost"
port = 3307
username = "root"
password = "root"
dbname = "student_management_system_1"

dbconnect = pymysql.connect(host=hostname,port=port,user=username,password=password,database=dbname)

if dbconnect.open:
    query = "select * from emp_details"
    cursor = dbconnect.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)