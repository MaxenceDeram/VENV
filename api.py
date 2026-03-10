from flask import Flask
import mysql.connector
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def hello_world():

    return "<p>Hello, World!</p>"

@app.route("/users", methods=["GET"])
def get_users():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    mycursor = mydb.cursor()

    mycursor.execute("USE api_example")
    mycursor.execute("SELECT * FROM users")

    # Fetch all users and return them as a JSON response
    users = mycursor.fetchall()
    return {"users": [{"id": user[0], "name": user[1], "email": user[2]} for user in users]}

@app.route("/users", methods=["POST"])
def create_user():

    data = request.json
    name = data.get("name")
    email = data.get("email")
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    mycursor = mydb.cursor()

    mycursor.execute("USE api_example")
    mycursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    mydb.commit()
    
    return {"message": f"User {name} created successfully!"}

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    name = data.get("name")
    email = data.get("email")
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    mycursor = mydb.cursor()
    mycursor.execute("USE api_example")
    mycursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
    mydb.commit()
    return {"message": f"User with id {user_id} updated successfully!"}


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    mycursor = mydb.cursor()
    mycursor.execute("USE api_example")
    mycursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mydb.commit()
    return {"message": f"User with id {user_id} deleted successfully!"}
