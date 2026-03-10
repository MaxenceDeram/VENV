import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

mycursor = mydb.cursor()

mycursor.execute("USE api_example")

for i in range(10):
    mycursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (f"Client {i}", f"client{i}@example.com"))

mydb.commit()