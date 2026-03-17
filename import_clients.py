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
        query = """
        INSERT INTO clients_import (
            client_id, first_name, last_name, gender, age,
            height_cm, weight_kg, bmi, size_code, recommended_size
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            int(row["customer_id"]),
            row["first_name"],
            row["last_name"],
            row["gender"],
            int(row["age"]),
            float(row["height_cm"]),
            float(row["weight_kg"]),
            float(row["bmi"]),
            int(row["size_code"]),
            row["recommended_size"]
        )
        cursor.execute(query, values)

conn.commit()
cursor.close()
conn.close()

print("Import terminé dans clients_import.")