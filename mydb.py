


import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
)

#prepare cursor
cursorObject = dataBase.cursor()

#create the database

cursorObject.execute("CREATE DATABASE test")
print("ALL DONE!")