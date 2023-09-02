# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='200210',
)

#prepare a cursor object

cursorObject = database.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE GSP")

print('U DID IT GANESH , GURU KRUPA')