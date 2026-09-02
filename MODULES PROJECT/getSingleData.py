from dbConnection import connection

dbconnect = connection()

if type(dbconnect).__name__!="bool":
    query = "select * from emp_details where id=4"
    cursor = dbconnect.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    print(data)
else:
    print("something went wrong")