import mysql.connector

class ORM:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def select_all(self, table):
        conn = None
        cursor = None
        try:
            conn = self.connect()
            cursor = conn.cursor(dictionary=True)
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            return cursor.fetchall()

        except mysql.connector.Error as err:
            return {"erreur": str(err)}

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def select_by_id(self, table, id_column, id_value):
        conn = None
        cursor = None
        try:
            conn = self.connect()
            cursor = conn.cursor(dictionary=True)
            query = f"SELECT * FROM {table} WHERE {id_column} = %s"
            cursor.execute(query, (id_value,))
            return cursor.fetchone()

        except mysql.connector.Error as err:
            return {"erreur": str(err)}

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def insert(self, table, data):
        conn = None
        cursor = None
        try:
            conn = self.connect()
            cursor = conn.cursor()

            columns = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            values = tuple(data.values())

            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, values)
            conn.commit()

            return {
                "message": "Insertion réussie",
                "last_id": cursor.lastrowid
            }

        except mysql.connector.Error as err:
            return {"erreur": str(err)}

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def update(self, table, id_column, id_value, data):
        conn = None
        cursor = None
        try:
            conn = self.connect()
            cursor = conn.cursor()

            set_clause = ", ".join([f"{col} = %s" for col in data.keys()])
            values = list(data.values())
            values.append(id_value)

            query = f"UPDATE {table} SET {set_clause} WHERE {id_column} = %s"
            cursor.execute(query, tuple(values))
            conn.commit()

            if cursor.rowcount == 0:
                return {"message": "Aucune ligne modifiée"}

            return {"message": "Mise à jour réussie"}

        except mysql.connector.Error as err:
            return {"erreur": str(err)}

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def delete(self, table, id_column, id_value):
        conn = None
        cursor = None
        try:
            conn = self.connect()
            cursor = conn.cursor()

            query = f"DELETE FROM {table} WHERE {id_column} = %s"
            cursor.execute(query, (id_value,))
            conn.commit()

            if cursor.rowcount == 0:
                return {"message": "Aucune ligne supprimée"}

            return {"message": "Suppression réussie"}

        except mysql.connector.Error as err:
            return {"erreur": str(err)}

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()