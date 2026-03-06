from typing import Any

from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector.abstracts import MySQLCursorAbstract

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/info', methods=['GET'])
def info():
    return jsonify({'jaime trop les filles': 'je suis un homme'})

@app.route('/products', methods=['GET'])
def get_products():
    conn = mysql.connector.connect(
        host="mysql-maxderam.alwaysdata.net",
        user="maxderam",
        password="MDP",
        database="maxderam_projectclothingv1"
    )

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM catalog")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(products)

@app.route('/clients', methods=['GET'])
def get_clients():
    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="mysql-maxderam.alwaysdata.net",
        user="maxderam",
        password="MDP",
        database="maxderam_projectclothingv1"
    )

    # Récupération des clients
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()

    # Fermeture de la connexion
    cursor.close()
    conn.close()

    # Retour des clients au format JSONS
    return jsonify(clients)

# Routes pour ajouter, mettre à jour et supprimer des clients
@app.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json()
    # Ici, vous pouvez ajouter le code pour insérer les données dans la base de données
    conn = mysql.connector.connect(
        host="mysql-maxderam.alwaysdata.net",
        user="maxderam",
        password="MDP",
        database="maxderam_projectclothingv1"
    )
    
    cursor = conn.cursor()# Relie la connexion à la base de données et crée un curseur pour exécuter des requêtes SQL
    cursor.execute ("INSERT INTO clients (first_name, last_name, email, phone, city, country) VALUES (%s, %s, %s, %s, %s, %s)",
        (data['first_name'], data['last_name'], data['email'], data['phone'], data['city'], data['country']) 
    )
    
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Client added successfully!'}) 

@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.get_json()
    conn = mysql.connector.connect(
        host="mysql-maxderam.alwaysdata.net",
        user="maxderam",
        password="MDP",
        database="maxderam_projectclothingv1"
    )
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE clients SET first_name = %s, last_name = %s, email = %s, phone = %s, city = %s, country = %s WHERE client_id = %s",
        (data['first_name'], data['last_name'], data['email'], data['phone'], data['city'], data['country'], client_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Client updated successfully!'})

@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    conn = mysql.connector.connect(
        host="mysql-maxderam.alwaysdata.net",
        user="maxderam",
        password="MDP",
        database="maxderam_projectclothingv1"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE client_id = %s", (client_id,))
    conn.commit()
    cursor.close()
    conn.close()
   
    return jsonify({'message': 'Client deleted successfully!'})

@app.route('/stats', methods=['GET'])
def get_stats():
    conn = mysql.connector.connect(
        host="mysql-maxderam.alwaysdata.net",
        user="maxderam",
        password="MDP",
        database="maxderam_projectclothingv1"
    )

    cursor = conn.cursor(dictionary=True)

if __name__ == "__main__":
    app.run(debug=True)