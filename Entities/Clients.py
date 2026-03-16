class Clients:

    def __init__(self, client_id, first_name, last_name, email, phone, city, country, created_at):

        self.__client_id = client_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__city = city
        self.__country = country
        self.__created_at = created_at

    def get_client_id(self):
        return self.__client_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_city(self):
        return self.__city

    def get_country(self):
        return self.__country

    def get_created_at(self):
        return self.__created_at