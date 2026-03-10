import mysql


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

    def use_database(self, mydb):
        mycursor = mydb.cursor()
        mycursor.execute(f"USE {self.database}")

    def select_all(self, table):
        mydb = self.connect()
        self.use_database(mydb)
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM {table}")
        return mycursor.fetchall()

my_orm = ORM(host="mysql-maxderam.alwaysdata.net", user="maxderam", password="MDP", database="api_example")
my_orm.connect()
my_orm.select_all("users")