import mysql.connector

mydb = mysql.connector.connect(
  hhost="mysql-maxderam.alwaysdata.net",
        user="maxderam",
        password="MDP",
        database="maxderam_projectclothingv1"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS api_example")
mycursor.execute("USE api_example")
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")