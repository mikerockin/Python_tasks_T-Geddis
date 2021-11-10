class Person:
    def __init__(self, name, address, pnone_n):
        self.__name = name
        self.__address = address
        self.__phone_n = pnone_n

    def set_name(self, name):
        self.__name = name
    def set_address(self, addreess):
        self.__address = addreess
    def set_phone(self, phone_n):
        self.__phone_n = phone_n

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone_n(self):
        return self.__phone_n

class Customer(Person):
    def __init__(self, name, address, phone_n, client_number, spam):

        Person.__init__(self, name, address, phone_n)

        self.__client_number = client_number
        self.__spam = spam

    def set_client_number(self, client_number):
        self.__client_number = client_number

    def set_spam(self,spam):
        self.__spam = spam

    def get_client_number(self):
        return self.__client_number

    def get_spam(self):
        return self.__spam
