
from dbConnection import connection

dbconnect = connection()

if type(dbconnect).__name__!="bool":
    query = "update emp_details set name='Aditya Sharma',email='aditya@gmail.com' where id=1"
    cursor = dbconnect.cursor()
    cursor.execute(query)
    dbconnect.commit()
    print("Record Updated")
else:
    print("something went wrong")