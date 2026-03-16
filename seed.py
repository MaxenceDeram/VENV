# This script is used to seed the database with initial data for testing purposes. (en cours)

import mysql.connector

mydb = mysql.connector.connect(
  host="mysql-maxderam.alwaysdata.net",
        user="maxderam",
        password="MDP",
        database="maxderam_projectclothingv1"
)

mycursor = mydb.cursor()

mycursor.execute("USE api_example")

for i in range(10):
    mycursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (f"Client {i}", f"client{i}@example.com"))

mydb.commit()