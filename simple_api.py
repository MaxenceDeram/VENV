from flask import Flask, jsonify, request
import mysql.connector

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
    conn = mysql.connector.connect(
        host="mysql-maxderam.alwaysdata.net",
        user="maxderam",
        password="MDP",
        database="maxderam_projectclothingv1"
    )

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(clients)

@app.route('/clients', methods=['POST'])
def add_client():
   return jsonify({'message': 'Client added successfully!'}) 

@app.route('/clients', methods=['PUT'])
def update_client():
   return jsonify({'message': 'Client updated successfully!'}) 

@app.route('/clients', methods=['PUT'])
def delete_client():
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