import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "Password1!",)



dbcursor = db.cursor()
#dbcursor.execute("CREATE DATABASE Appdata1")
#dbcursor.execute("SHOW DATABASES")
#print(dbcursor.execute("SHOW DATABASES"))