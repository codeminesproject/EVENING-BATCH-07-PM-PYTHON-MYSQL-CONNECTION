"""
If we want to connect VS Code with MySQL then we will use library(module) pymysql

install pymysql (one time)
pip install pymysql
"""

import pymysql

# step 1: build connectivity between vs code and mysql

hostname = "localhost"
port = 3307
username = "root"
password = "root"
dbname = "student_management_system_1"

dbconnect = pymysql.connect(host=hostname,port=port,user=username,password=password,database=dbname)

print(dbconnect.open)

