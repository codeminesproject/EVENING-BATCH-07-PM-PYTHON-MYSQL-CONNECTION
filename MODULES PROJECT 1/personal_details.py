
from dbOperation import insert

def insertData():
    query = "insert into personal_details(name,gender,email,mobile,address) values('Vedant Pawar','Male','vedant@gmail.com','1234567890','Mumbai')"
    response = insert(query)
    if response==True:
        print("Record Inserted")
    else:
        print("Insertion failed")

insertData()
