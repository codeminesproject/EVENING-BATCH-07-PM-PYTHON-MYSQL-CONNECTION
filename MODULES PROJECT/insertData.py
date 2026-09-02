
from dbConnection import connection

dbconnect = connection()

if type(dbconnect).__name__!="bool":
    query = "insert into emp_details(name,email) values('Ramesh Patil','rameshp@gmail.com')"
    cursor = dbconnect.cursor()
    cursor.execute(query)
    dbconnect.commit()
    print("Record Inserted")
else:
    print("something went wrong")