class Client:
    def __init__(self, client_id, first_name, last_name, email, phone, city, country, created_at ):
        self.__client_id = client_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__city = city
        self.__country = country
        self.__created_at = created_at 

    def get_email(self):
        return self.__email

client1 = Client(1, "John", "Doe", "john.doe@example.com", "123456789", "New York", "USA", "2023-01-01")
print(client1.get_email())

