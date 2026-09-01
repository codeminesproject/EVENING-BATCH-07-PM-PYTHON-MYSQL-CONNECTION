import pymysql

hostname = "localhost"
port = 3307
username = "root"
password = "root"
dbname = "student_management_system_1"

dbconnect = pymysql.connect(host=hostname,port=port,user=username,password=password,database=dbname)

if dbconnect.open:
    query = "update emp_details set name='Aditya Sharma',email='aditya@gmail.com' where id=1"
    cursor = dbconnect.cursor()
    cursor.execute(query)
    dbconnect.commit()
    print("Record Updated")