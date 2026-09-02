
from dbConnection import connection

dbconnect = connection()

if type(dbconnect).__name__!="bool":
    query = "delete from emp_details where id=2"
    cursor = dbconnect.cursor()
    cursor.execute(query)
    dbconnect.commit()
    print("Record Deleted")
else:
    print("something went wrong")