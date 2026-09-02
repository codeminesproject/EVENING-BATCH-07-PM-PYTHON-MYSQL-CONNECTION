from dbConnection import connection

dbconnect = connection()

if type(dbconnect).__name__!="bool":
    query = "select * from emp_details"
    cursor = dbconnect.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
else:
    print("something went wrong")