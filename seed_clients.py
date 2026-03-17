import csv
import mysql.connector

conn = mysql.connector.connect(
    host="mysql-maxderam.alwaysdata.net",
    user="maxderam_prune",
    password="Prune59.",
    database="maxderam_projectclothingv1"
)

cursor = conn.cursor()

with open("clothing_clients_100.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        client_id = int(row["customer_id"])
        first_name = row["first_name"]
        last_name = row["last_name"]
        gender = row["gender"]
        age = int(row["age"])
        height_cm = float(row["height_cm"])
        weight_kg = float(row["weight_kg"])
        bmi = float(row["bmi"])
        size_code = int(row["size_code"])
        recommended_size = row["recommended_size"]
        email = f"client{client_id}@gmail.com"

        # 1) vérifier si le client existe déjà
        cursor.execute(
            "SELECT client_id FROM clients WHERE client_id = %s",
            (client_id,)
        )
        existing_client = cursor.fetchone()

        if existing_client:
            # 2) UPDATE
            update_query = """
            UPDATE clients
            SET
                first_name = %s,
                last_name = %s,
                gender = %s,
                age = %s,
                height_cm = %s,
                weight_kg = %s,
                bmi = %s,
                size_code = %s,
                recommended_size = %s
            WHERE client_id = %s
            """
            update_values = (
                first_name,
                last_name,
                gender,
                age,
                height_cm,
                weight_kg,
                bmi,
                size_code,
                recommended_size,
                client_id
            )
            cursor.execute(update_query, update_values)

        else:
            # 3) INSERT
            insert_query = """
            INSERT INTO clients (
                client_id,
                first_name,
                last_name,
                gender,
                age,
                height_cm,
                weight_kg,
                bmi,
                size_code,
                recommended_size,
                email,
                phone,
                city,
                country
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            insert_values = (
                client_id,
                first_name,
                last_name,
                gender,
                age,
                height_cm,
                weight_kg,
                bmi,
                size_code,
                recommended_size,
                email,
                None,
                None,
                "France"
            )
            cursor.execute(insert_query, insert_values)

conn.commit()
cursor.close()
conn.close()

print("Import + update terminé.")
        
