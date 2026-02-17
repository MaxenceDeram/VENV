from flask import Flask, jsonify, request
from flask import Flask, jsonify, request, render_template
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

    # nombre total de produits
    cursor.execute("SELECT COUNT(*) AS total_products FROM catalog")
    total_products = cursor.fetchone()

    # valeur totale du stock
    cursor.execute("SELECT SUM(stock * price_eur) AS stock_value FROM catalog")
    stock_value = cursor.fetchone()

    # nombre total de clients
    cursor.execute("SELECT COUNT(*) AS total_clients FROM clients")
    total_clients = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify({
        "total_products": total_products["total_products"],
        "stock_value_eur": stock_value["stock_value"],
        "total_clients": total_clients["total_clients"]
    })

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)