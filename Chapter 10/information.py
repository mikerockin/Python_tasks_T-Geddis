# -*- coding: utf8 -*-
class Information:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
    def set_name(self):
        self.__name = name
    def set_adress(self):
        self.__address = address
    def set_age(self):
        self.__age = age
    def set_phone(self):
        self.__phone = phone
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone(self):
        return self.__phone

