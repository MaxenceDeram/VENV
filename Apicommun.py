import mysql.connector
from flask import Flask, jsonify, request
from Entities.Clients import Clients

app = Flask(__name__)

db_config = {
    'host': 'mysql-maxderam.alwaysdata.net',
    'user': 'maxderam_prune',
    'password': 'Prune59.',
    'database': 'maxderam_projectclothingv1'
}


@app.route('/catalog', methods=['GET'])
def recuperer_vetement():

    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM catalog")
        rows = cursor.fetchall()

        return jsonify(rows)

    except mysql.connector.Error as err:
        return jsonify({"erreur": f"Connexion échouée : {err}"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/catalog/<int:product_id>', methods=['GET'])
def recuperer_vetement_par_id(product_id):

    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM catalog WHERE product_id = %s", (product_id,))
        row = cursor.fetchone()

        if not row:
            return jsonify({"message": "Produit introuvable"}), 404

        return jsonify(row)

    except mysql.connector.Error as err:
        return jsonify({"erreur": str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/catalog', methods=['POST'])
def ajouter_vetement():

    conn = None
    cursor = None

    try:
        data = request.get_json()

        product_name = data['product_name']
        category = data['category']
        color = data['color']
        size = data['size']
        price_eur = data['price_eur']
        stock = data['stock']
        product_code = data['product_code']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = """
        INSERT INTO catalog 
        (product_name, category, color, size, price_eur, stock, product_code)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            product_name,
            category,
            color,
            size,
            price_eur,
            stock,
            product_code
        ))

        conn.commit()

        return jsonify({"message": "Produit ajouté"}), 201

    except mysql.connector.Error as err:
        return jsonify({"erreur": str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/catalog/<int:product_id>', methods=['PUT'])
def modifier_vetement(product_id):

    conn = None
    cursor = None

    try:
        data = request.get_json()

        product_name = data['product_name']
        category = data['category']
        color = data['color']
        size = data['size']
        price_eur = data['price_eur']
        stock = data['stock']
        product_code = data['product_code']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = """
        UPDATE catalog
        SET product_name = %s,
            category = %s,
            color = %s,
            size = %s,
            price_eur = %s,
            stock = %s,
            product_code = %s
        WHERE product_id = %s
        """

        cursor.execute(query, (
            product_name,
            category,
            color,
            size,
            price_eur,
            stock,
            product_code,
            product_id
        ))

        conn.commit()

        return jsonify({"message": "Produit modifié"}), 200

    except mysql.connector.Error as err:
        return jsonify({"erreur": str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/catalog/<int:product_id>', methods=['DELETE'])
def supprimer_vetement(product_id):

    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "DELETE FROM catalog WHERE product_id = %s"
        cursor.execute(query, (product_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Produit introuvable"}), 404

        return jsonify({"message": "Produit supprimé"}), 200

    except mysql.connector.Error as err:
        return jsonify({"erreur": str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/clients', methods=['GET'])
def recuperer_clients():

    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM clients")
        rows = cursor.fetchall()

        clients = []

        for row in rows:
            client = Clients(
                row["client_id"],
                row["first_name"],
                row["last_name"],
                row["email"],
                row["phone"],
                row["city"],
                row["country"],
                row["created_at"]
            )
            print(client.get_email())
            
            clients.append({
                "client_id": client.get_client_id(),
                "first_name": client.get_first_name(),
                "last_name": client.get_last_name(),
                "email": client.get_email(),
                "phone": client.get_phone(),
                "city": client.get_city(),
                "country": client.get_country(),
                "created_at": client.get_created_at()
            })

        return jsonify(clients)

    except mysql.connector.Error as err:
        return jsonify({"erreur": str(err)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)