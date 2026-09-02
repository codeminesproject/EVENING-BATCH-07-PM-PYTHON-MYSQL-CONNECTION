
from dbOperation import insert

def insertData():
    query = "insert into emp_details(name,email) values('Vedant Pawar','vedant@gmail.com')"
    response = insert(query)
    if response==True:
        print("Record Inserted")
    else:
        print("Insertion failed")

insertData()
