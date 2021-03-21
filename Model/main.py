import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="PZZwsmapE4-Uk:6",
    database="testdb",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")