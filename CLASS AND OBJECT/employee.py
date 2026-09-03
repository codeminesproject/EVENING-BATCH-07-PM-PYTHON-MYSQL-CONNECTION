
from dbWrapper import DBOperation

def insertData():
    query = "insert into emp_details(name,email) values('Vedant Pawar','vedant@gmail.com')"
    response = DBOperation.insert(query)
    if response==True:
        print("Record Inserted")
    else:
        print("Insertion failed")

insertData()